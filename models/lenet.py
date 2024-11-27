from plotnn import *
from pathlib import Path

arch = [
    Picture(pathfile="../assets/mnist8.png",to="(-2,0,0)", height=220, width=295,name=''), 
    Input(name="input", caption="", shape=(1,28,28), size=(1,30,30), offset="(-2,-0.04,0.1)", to="(0,0,0)"),
    ConvRelu(name="conv1", caption="Conv1+Sigmoid", shape=(6,28,28), size=(3,30,30), offset="(0,0,0)", to="(0,0,0)"),
    Pool(name="pool1", caption="AvgPool1", shape=(6,14,14), size=(3,20,20), offset="(0,0,0)", to="(conv1-east)", titlepos=-25),
    ConvRelu(name="conv2", caption="Conv2+Sigmoid", shape=(16,10,10), size=(3,20,20), offset="(2,0,0)", to="(pool1-east)"),
    Pool(name="pool2", caption="AvgPool2", shape=(16,5,5), size=(3,10,10), offset="(0,0,0)", to="(conv2-east)", titlepos=-25),
    FullyConnected(name="FCN1", caption="FCN1", shape=('','',120), size=(1,1,25), offset="(1.5,0,0)",to="(pool2-east)"),
    FullyConnected(name="FCN2", caption="FCN2", shape=('','',84), size=(1,1,18), offset="(1.5,0,0)",to="(FCN1-east)"),
    SoftMax(name="soft", caption="Softmax", shape=('','',10) ,size=(1,1,10), offset="(1.5,0,0)",to="(FCN2-east)"),
    Connection(of="pool1", to="conv2", label=""),
    Connection(of="pool2", to="FCN1", label=""), 
    Connection(of="FCN1", to="FCN2", label=""),
    Connection(of="FCN2", to="soft", label="")
    ]

if __name__ == '__main__':
    generate(arch, f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)
