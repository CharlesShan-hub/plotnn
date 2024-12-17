
import os

def latexful(func):
    def wrapper(*args, **kwargs):
        if 'caption' in kwargs:
            # 替换 caption 参数中的 '\n' 为 '\newline'
            kwargs['caption'] = kwargs['caption'].replace("\n", "\\newline ")
        return func(*args, **kwargs)
    return wrapper
    
def Head( projectpath, border=8):
    pathlayers = os.path.join( projectpath, 'layers/' ).replace('\\', '/')
    return r"""
\documentclass[border="""+ str(border) + r"""pt, multi, tikz]{standalone}
\usepackage{import}
\subimport{"""+ pathlayers + r"""}{init}
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

# layers definition

def Picture( pathfile, to='(-3,0,0)', width=8, height=8, name="temp" ):
    return r"""
\node[canvas is zy plane at x=0] (""" + name + """) at """+ to +""" {\includegraphics[width="""+ str(width)+"px"+""",height="""+ str(height)+"px"+"""]{"""+ pathfile +"""}};
"""

# Conv
# def to_Conv( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" ", titlepos=0 ):
@latexful
def Input( name, s_filer=(256,256), n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=32, height=32, depth=1, caption=" ", titlepos=0):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +"""
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        ylabel="""+ str(s_filer[1]) +""",
        zlabel="""+ str(s_filer[0]) +""",
        fill=\InputColor,
        height="""+ str(height) +""",
        width="""+ str(depth) +""",
        depth="""+ str(width) +"""
        }
    };
"""

# Conv
# def to_Conv( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" ", titlepos=0 ):
@latexful
def Conv( name, s_filer=(256,256), n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=32, height=32, depth=3, caption=" ", titlepos=0 ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +"""
    {Box={
        name=""" + name +""",
        caption="""+ caption +r""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        ylabel="""+ str(s_filer[1]) +""",
        zlabel="""+ str(s_filer[0]) +""",
        fill=\ConvColor,
        height="""+ str(height) +""",
        width="""+ str(depth) +""",
        depth="""+ str(width) +"""
        }
    };
"""


def ConvRelu( name, s_filer=(256,256), n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=40, height=40, depth=2, caption=" ", titlepos=0):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +"""
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{ """+ str(n_filer) +""", """+ " " +""" }},
        ylabel="""+ str(s_filer[1]) +""",
        zlabel="""+ str(s_filer[0]) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(depth) +""" , """+ str(0) +""" },
        depth="""+ str(width) +"""
        }
    };
"""

def ConvConvRelu( name, s_filer=(256,256), n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=40, height=40, depth=2, caption=" ", titlepos=0):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +"""
    {RightBandedBox={
        name="""+ name +""",
        caption="""+ caption +""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{ """+ str(n_filer[0]) +""", """+ str(n_filer[1]) +""" }},
        ylabel="""+ str(s_filer[1]) +""",
        zlabel="""+ str(s_filer[0]) +""",
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height="""+ str(height) +""",
        width={ """+ str(depth) +""" , """+ str(0) +""" },
        depth="""+ str(width) +"""
        }
    };
"""



# Pool
# def to_Pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" ", titlepos=0):
@latexful
def Pool(name, s_filer=(256,256), n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=32, height=32, depth=2, opacity=0.5, caption=" ", titlepos=0):
    print(caption)
    
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +"""
    {Box={
        name="""+name+""",
        caption="""+ caption +r""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{"""+ str(n_filer) +""", }},
        ylabel="""+ str(s_filer[1]) +""",
        zlabel="""+ str(s_filer[0]) +""",
        fill=\PoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(depth) +""",
        depth="""+ str(width) +"""
        }
    };
"""

# unpool4,
def UnPool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" ", titlepos=0):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +"""
    {Box={
        name="""+ name +r""",
        caption="""+ caption +r""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        fill=\UnpoolColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""



def ConvRes( name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2, caption=" ", titlepos=0 ):
    return r"""
\pic[shift={ """+ offset +""" }] at """+ to +"""
    {RightBandedBox={
        name="""+ name + """,
        caption="""+ caption + """,
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{ """+ str(n_filer) + """, }},
        zlabel="""+ str(s_filer) +r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""


# ConvSoftMax
def ConvSoftMax( name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" ", titlepos=0 ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +"""
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

# SoftMax
def SoftMax( name, s_filer=10, offset="(0,0,0)", to="(0,0,0)", width=2, height=2, depth=25, opacity=0.8, caption=" ", titlepos=0 ):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +"""
    {Box={
        name=""" + name +""",
        caption="""+ caption +""",
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{" ","dummy"}},
        zlabel="""+ str(s_filer) +""",
        fill=\SoftmaxColor,
        opacity="""+ str(opacity) +""",
        height="""+ str(height) +""",
        width="""+ str(width) +""",
        depth="""+ str(depth) +"""
        }
    };
"""

def Sum( name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    return r"""
\pic[shift={"""+ offset +"""}] at """+ to +"""
    {Ball={
        name=""" + name +""",
        fill=\SumColor,
        opacity="""+ str(opacity) +""",
        radius="""+ str(radius) +""",
        logo=$+$
        }
    };
"""

def FullyConnected(name, n_filer=120, offset="(0,0,0)", to="(0,0,0)", width=2, height=2, depth=10, caption=" ", titlepos=0):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """
    {Box={
        name=""" + name + """,
        caption=""" + caption + """,
        titlepos="""+ str(titlepos-25) + "px" +r""",
        xlabel={{" ","dummy"}},
        zlabel=""" + str(n_filer) + """,
        fill=\FcColor,
        opacity=0.8,
        height=""" + str(height) + """,
        width=""" + str(width) + """,
        depth=""" + str(depth) + """
        }
    };
"""

# def to_connection( of, to):
#     return r"""
# \draw [connection]  ("""+of+"""-east)    -- node {\midarrow} ("""+to+"""-west);
# """
def Connection(of, to, label=""):
    label = label.replace("\n", "\\newline ")
    return r"""
\draw [connection,->] ("""+of+"""-east) -- node[midway, above] {\parbox{2cm}{"""+label+"""}} ("""+to+"""-west);
"""

def Skip( of, to, pos=1.25):
    return r"""
\path ("""+ of +"""-southeast) -- ("""+ of +"""-northeast) coordinate[pos="""+ str(pos) +"""] ("""+ of +"""-top) ;
\path ("""+ to +"""-south)  -- ("""+ to +"""-north)  coordinate[pos="""+ str(pos) +"""] ("""+ to +"""-top) ;
\draw [copyconnection]  ("""+of+"""-northeast)
-- node {\copymidarrow}("""+of+"""-top)
-- node {\copymidarrow}("""+to+"""-top)
-- node {\copymidarrow} ("""+to+"""-north);
"""

def End():
    return r"""
\end{tikzpicture}
\end{document}
"""


def generate( arch, projectpath='..', pathname="file.tex", border=8):
    with open(pathname, "w") as f:
        for c in [Head(projectpath, border=border),Cor(),Begin()]+arch+[End()]:
            print(c)
            f.write( c )
