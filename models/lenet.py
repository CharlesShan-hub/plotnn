from plotnn import *
from pathlib import Path

arch = [
    Picture("../assets/mnist8.png",to="(-2,0,0)", height=225, width=275), 
    Input("input", (28,28), 1, offset="(-2,0,0)", height=30, width=30, depth=1),
    ConvRelu("conv1", (28,28), 6, caption="Conv1+Sigmoid", offset="(0,0,0)", to="(0,0,0)", height=30, width=30, depth=3),
    Pool("pool1", (14,14), 6, caption="AvgPool1", offset="(0,0,0)", to="(conv1-east)", height=20, width=20, depth=3, titlepos=-25),
    ConvRelu("conv2", (10,10), 16,caption="Conv2+Sigmoid",  offset="(2,0,0)", to="(pool1-east)", height=20, width=20, depth=3),
    Pool("pool2", (5,5), 16, caption="AvgPool2",offset="(0,0,0)", to="(conv2-east)", height=10, width=10, depth=3, titlepos=-25),
    FullyConnected("FCN1", n_filer=120, caption="FCN1", offset="(6,0,0)", depth=25),
    FullyConnected("FCN2", n_filer=84, caption="FCN2", offset="(7.5,0,0)", depth=18),
    SoftMax("soft", 10 ,"(9,0,0)", caption="Softmax", depth=10),
    Connection("pool1", "conv2"),
    Connection("pool2", "FCN1"), 
    Connection("FCN1", "FCN2"),
    Connection("FCN2", "soft")
    ]

if __name__ == '__main__':
    generate(arch, '.', f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)