from plotnn import *
from pathlib import Path

arch = [
    Picture(pathfile="../assets/cats.jpg",to="(-2,0,0)", height=225, width=225, name=''), 
    Input(name="input", caption="", shape=(3,224,224), size=(2,40,40), offset="(-2,0,0)", to="(0,0,0)"),
    ConvRelu(name="conv1", caption="", shape=(96,54,54), size=(3,40,40), offset="(0,0,0)", to="(0,0,0)"),
    Pool(name="pool1", caption="", shape=(96,26,26), size=(3,30,30), offset="(0,0,0)", to="(conv1-east)", titlepos=-25),
    ConvRelu(name="conv2", caption="", shape=(256,26,26), size=(4,30,30), offset="(2.5,0,0)", to="(pool1-east)"),
    Pool(name="pool2", caption="", shape=(12,12,256), size=(4,20,20), offset="(0,0,0)", to="(conv2-east)", titlepos=-25),
    ConvRelu(name="conv31", caption="", shape=(256,'',''), size=(4,20,20), offset="(2,0,0)", to="(pool2-east)"),
    ConvRelu(name="conv32", caption="", shape=(256,'',''), size=(4,20,20), offset="(0,0,0)", to="(conv31-east)"),
    ConvRelu(name="conv33", caption="", shape=(256,26,26), size=(4,20,20), offset="(0,0,0)", to="(conv32-east)"),
    Pool(name="pool3", caption="",  shape=(256,12,12), size=(4,8,8),offset="(0,0,0)", to="(conv33-east)", titlepos=-25),
    FullyConnected(name="FCN1", caption="FCN", shape=('','',6400), size=(1,1,30), offset="(1.5,0,0)", to="(pool3-east)"),
    FullyConnected(name="FCN2", caption="FCN", shape=('','',4096), size=(1,1,23), offset="(1.5,0,0)", to="(FCN1-east)"),
    SoftMax(name="soft", caption="Softmax", shape=('','',1000), size=(1,1,15), offset="(1.5,0,0)", to="(FCN2-east)"),
    Connection(of="pool1", to="conv2", label=''),
    Connection(of="pool2", to="conv31", label=''),
    Connection(of="pool3", to="FCN1", label=''), 
    Connection(of="FCN1", to="FCN2", label=''),
    Connection(of="FCN2", to="soft", label='')
]

if __name__ == '__main__':
    generate(arch, f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)
