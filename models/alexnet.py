from plotnn import *
from pathlib import Path

arch = [
    Picture("../assets/cats.jpg",to="(-2,0,0)", height=220, width=220), 
    Input("input", (224,224), 3, offset="(-2,0,0)", height=40, width=40, depth=2),
    ConvRelu("conv1", (54,54), 96, caption="Conv1+ReLU", offset="(0,0,0)", to="(0,0,0)", height=40, width=40, depth=3),
    Pool("pool1", (26,26), 96, caption="MaxPool1", offset="(0,0,0)", to="(conv1-east)", height=30, width=30, depth=3, titlepos=-25),
    ConvRelu("conv2", (26,26), 256,caption="Conv2+ReLU",  offset="(3,0,0)", to="(pool1-east)", height=30, width=30, depth=4),
    Pool("pool2", (12,12), 256, caption="MaxPool2",offset="(0,0,0)", to="(conv2-east)", height=20, width=20, depth=4, titlepos=-25),
    ConvRelu("conv31", (26,26), 256,caption="Conv3",  offset="(2,0,0)", to="(pool2-east)", height=20, width=20, depth=4),
    ConvRelu("conv32", (26,26), 256,caption="",  offset="(0,0,0)", to="(conv31-east)", height=20, width=20, depth=4),
    ConvRelu("conv33", (26,26), 256,caption="",  offset="(0,0,0)", to="(conv32-east)", height=20, width=20, depth=4),
    Pool("pool3", (12,12), 256, caption="MaxPool3",offset="(0,0,0)", to="(conv33-east)", height=10, width=10, depth=4, titlepos=-25),
    FullyConnected("FCN1", n_filer=6400, caption="FCN1", offset="(1.5,0,0)", to="(pool3-east)", depth=25),
    FullyConnected("FCN2", n_filer=4096, caption="FCN2", offset="(1.5,0,0)", to="(FCN1-east)", depth=18),
    SoftMax("soft", 1000 , offset="(1.5,0,0)", caption="Softmax", to="(FCN2-east)", depth=10),
    Connection("pool1", "conv2"),
    Connection("pool2", "conv31"),
    Connection("pool3", "FCN1"), 
    Connection("FCN1", "FCN2"),
    Connection("FCN2", "soft")
    ]

if __name__ == '__main__':
    generate(arch, '.', f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)