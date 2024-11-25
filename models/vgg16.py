from plotnn import *
from pathlib import Path

arch = [
    Picture("../assets/cats.jpg",to="(-2,0,0)", height=220, width=220), 
    Input("input", (224,224), 3, offset="(-2,0,0)", height=40, width=40, depth=2),
    
    ConvRelu("conv11", (224,224), 64, caption="", offset="(0,0,0)", to="(0,0,0)", height=40, width=40, depth=3),
    ConvRelu("conv12", (224,224), 64, caption="", offset="(0,0,0)", to="(conv11-east)", height=40, width=40, depth=3),
    Pool("pool1", (112,112), 64, caption="", offset="(0,0,0)", to="(conv12-east)", height=35, width=35, depth=3, titlepos=-25),
    
    ConvRelu("conv21", (112,112), 128, caption="", offset="(2,0,0)", to="(pool1-east)", height=35, width=35, depth=3),
    ConvRelu("conv22", (112,112), 128, caption="", offset="(0,0,0)", to="(conv21-east)", height=35, width=35, depth=3),
    Pool("pool2", (56,56), 128, caption="", offset="(0,0,0)", to="(conv22-east)", height=30, width=30, depth=3, titlepos=-25),
    
    ConvRelu("conv31", (56,56), 256, caption="", offset="(2,0,0)", to="(pool2-east)", height=30, width=30, depth=3),
    ConvRelu("conv32", (56,56), 256, caption="", offset="(0,0,0)", to="(conv31-east)", height=30, width=30, depth=3),
    ConvRelu("conv33", (56,56), 256, caption="", offset="(0,0,0)", to="(conv32-east)", height=30, width=30, depth=3),
    Pool("pool3", (28,28), 256, caption="", offset="(0,0,0)", to="(conv33-east)", height=25, width=25, depth=3, titlepos=-25),
    
    ConvRelu("conv41", (28,282), 512, caption="", offset="(2,0,0)", to="(pool3-east)", height=25, width=25, depth=3),
    ConvRelu("conv42", (28,28), 512, caption="", offset="(0,0,0)", to="(conv41-east)", height=25, width=25, depth=3),
    ConvRelu("conv43", (28,28), 512, caption="", offset="(0,0,0)", to="(conv42-east)", height=25, width=25, depth=3),
    Pool("pool4", (14,14), 512, caption="", offset="(0,0,0)", to="(conv43-east)", height=20, width=20, depth=3, titlepos=-25),

    ConvRelu("conv51", (14,14), 512, caption="", offset="(2,0,0)", to="(pool4-east)", height=20, width=20, depth=3),
    ConvRelu("conv52", (14,14), 512, caption="", offset="(0,0,0)", to="(conv51-east)", height=20, width=20, depth=3),
    ConvRelu("conv53", (14,14), 512, caption="", offset="(0,0,0)", to="(conv52-east)", height=20, width=20, depth=3),
    Pool("pool5", (7,7), 512, caption="", offset="(0,0,0)", to="(conv53-east)", height=15, width=15, depth=3, titlepos=-25),
    
    FullyConnected("FCN1", n_filer=4096, caption="", offset="(1.5,0,0)", to="(pool5-east)", depth=25),
    FullyConnected("FCN2", n_filer=4096, caption="", offset="(1.5,0,0)", to="(FCN1-east)", depth=25),
    FullyConnected("FCN3", n_filer=1000, caption="", offset="(1.5,0,0)", to="(FCN2-east)", depth=18),
    SoftMax("soft", 1000 , offset="(1.5,0,0)", caption="Softmax", to="(FCN3-east)", depth=10),
    
    Connection("pool1", "conv21"),
    Connection("pool2", "conv31"),
    Connection("pool3", "conv41"),
    Connection("pool4", "conv51"),
    Connection("pool5", "FCN1"), 
    Connection("FCN1", "FCN2"),
    Connection("FCN2", "FCN3"),
    Connection("FCN3", "soft")
    ]

if __name__ == '__main__':
    generate(arch, '.', f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)