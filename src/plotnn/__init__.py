from pathlib import Path

def Head(border=8):
    pathlayers = Path.cwd() / 'layers'
    return r"""
\documentclass[border="""+ str(border) + r"""pt, multi, tikz]{standalone}
\usepackage{import}
\subimport{"""+ str(pathlayers) + r"""}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image
"""

def Cor():
    return r"""
\def\InputColor{rgb:gray,0.1;white,5}
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}
\def\SumColor{rgb:blue,5;green,15}
"""

def Begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""

def End():
    return r"""
\end{tikzpicture}
\end{document}
"""

class Layer:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def generate(self):
        raise NotImplementedError("Subclasses must implement this method")

class Connection(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assert hasattr(self,'of')     # from
        assert hasattr(self,'to')     # to
        assert hasattr(self,'label')  # label
    
    def generate(self):
        return r"""
\draw [connection,->] ("""+self.of+"""-east) -- node[midway, above] {\parbox{2cm}{"""+self.label+"""}} ("""+self.to+"""-west);
"""

class Picture(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assert hasattr(self,'pathfile') 
        assert hasattr(self,'to') 
        assert hasattr(self,'width') 
        assert hasattr(self,'height') 
        assert hasattr(self,'name') 
    def generate(self):
        return r"""
\node[canvas is zy plane at x=0] (""" + self.name + """) at """+ self.to +""" {\includegraphics[width="""+ str(self.width)+"px"+""",height="""+ str(self.height)+"px"+"""]{"""+ self.pathfile +"""}};
"""

class Box(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assert hasattr(self,'name')          # 真正的ID
        assert hasattr(self,'caption')       # 绘图的名称
        assert hasattr(self,'shape')         # 标记的(C,H,W)
        assert hasattr(self,'size')          # 绘图的(C,H,W)
        assert hasattr(self,'offset')        # 偏移量
        assert hasattr(self,'to')            # 偏移量对应的参考目标
        if hasattr(self,'titlepos')==False:  # 绘图的名称向上偏移量
            self.titlepos = 0
        self.titlepos -= 25
    
    def generate(self):
        return fr"""
\pic[shift={{{self.offset}}}] at {self.to}
    {{Box={{
        name={self.name},
        caption={self.caption},
        titlepos={self.titlepos}px,
        xlabel={{{self.shape[0]},}},
        ylabel={self.shape[1]},
        zlabel={self.shape[2]},
        depth={self.size[2]},
        height={self.size[1]},
        width={self.size[0]},
        fill={self.fill_color},
        }}
    }};
"""
    
class RightBandedBox(Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        assert hasattr(self,'name')          # 真正的ID
        assert hasattr(self,'caption')       # 绘图的名称
        assert hasattr(self,'shape')         # 标记的(C,H,W)
        assert hasattr(self,'size')          # 绘图的(C,H,W)
        assert hasattr(self,'offset')        # 偏移量
        assert hasattr(self,'to')            # 偏移量对应的参考目标
        if hasattr(self,'titlepos')==False:  # 绘图的名称向上偏移量
            self.titlepos = 0
        self.titlepos -= 25
    
    def generate(self):
        return fr"""
\pic[shift={{{self.offset}}}] at {self.to}
    {{RightBandedBox={{
        name={self.name},
        caption={self.caption},
        titlepos={self.titlepos}px,
        xlabel={{{self.shape[0]},}},
        ylabel={self.shape[1]},
        zlabel={self.shape[2]},
        depth={self.size[2]},
        height={self.size[1]},
        width={self.size[0]},
        fill={self.fill_color},
        bandfill={self.bandfill_color},
        }}
    }};
"""

class Input(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\InputColor"

class Conv(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\ConvColor"

class ConvRelu(RightBandedBox):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\ConvColor"
        self.bandfill_color = r"\ConvReluColor"

class Pool(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\PoolColor"

class UnPool(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\UnpoolColor"

class SoftMax(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\SoftmaxColor"

class FullyConnected(Box):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fill_color = r"\FcColor"

def generate(arch, pathname="file.tex", border=8):
    with open(pathname, "w") as f:
        f.write(Head(border=border))
        f.write(Cor())
        f.write(Begin())
        for layer in arch:
            f.write(layer.generate())
        f.write(End())