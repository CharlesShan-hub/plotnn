from plotnn import *
from pathlib import Path

arch = [
    Picture(pathfile="../assets/cats.jpg",to="(-4,0,0)", height=430, width=430, name=''), 
    Input(name="input", shape=(3,224,224), offset="(-4,0,0)", to="(0,0,0)", size=(2,75,75), caption=""),
    
    ConvRelu(name="conv11", shape=(64,'',''), caption="", offset="(0,0,0)", to="(0,0,0)", size=(3,75,75)),
    ConvRelu(name="conv12", shape=(64,224,224), caption="", offset="(0,0,0)", to="(conv11-east)", size=(3,75,75)),
    Pool(name="pool1", shape=(64,112,112), caption="", offset="(0,0,0)", to="(conv12-east)", size=(3,60,60)),
    
    ConvRelu(name="conv21", shape=(128,'',''), caption="", offset="(2,0,0)", to="(pool1-east)", size=(3,60,60)),
    ConvRelu(name="conv22", shape=(128,112,112), caption="", offset="(0,0,0)", to="(conv21-east)", size=(3,60,60)),
    Pool(name="pool2", shape=(128,56,56), caption="", offset="(0,0,0)", to="(conv22-east)", size=(3,45,45)),
    
    ConvRelu(name="conv31", shape=(256,'',''), caption="", offset="(2,0,0)", to="(pool2-east)", size=(3,45,45)),
    ConvRelu(name="conv32", shape=(256,'',''), caption="", offset="(0,0,0)", to="(conv31-east)", size=(3,45,45)),
    ConvRelu(name="conv33", shape=(256,56,56), caption="", offset="(0,0,0)", to="(conv32-east)", size=(3,45,45)),
    Pool(name="pool3", shape=(256,28,28), caption="", offset="(0,0,0)", to="(conv33-east)", size=(3,30,30)),
    
    ConvRelu(name="conv41", shape=(512,'',''), caption="", offset="(1.5,0,0)", to="(pool3-east)", size=(4,30,30)),
    ConvRelu(name="conv42", shape=(512,'',''), caption="", offset="(0,0,0)", to="(conv41-east)", size=(4,30,30)),
    ConvRelu(name="conv43",shape= (512,28,28), caption="", offset="(0,0,0)", to="(conv42-east)", size=(4,30,30)),
    Pool(name="pool4", shape=(512,14,14), caption="", offset="(0,0,0)", to="(conv43-east)", size=(4,15,15)),

    ConvRelu(name="conv51", shape=(512,'',''), caption="", offset="(2,0,0)", to="(pool4-east)", size=(4,15,15)),
    ConvRelu(name="conv52", shape=(512,'',''), caption="", offset="(0,0,0)", to="(conv51-east)", size=(4,15,15)),
    ConvRelu(name="conv53", shape=(512,14,14), caption="", offset="(0,0,0)", to="(conv52-east)", size=(4,15,15)),
    Pool(name="pool5", shape=(512,7,7), caption="", offset="(0,0,0)", to="(conv53-east)", size=(4,8,8)),
    
    FullyConnected(name="FCN1", shape=('','',4096), caption="", offset="(1.5,0,0)", to="(pool5-east)", size=(1,1,25)),
    FullyConnected(name="FCN2", shape=('','',4096), caption="", offset="(1.5,0,0)", to="(FCN1-east)", size=(1,1,25)),
    FullyConnected(name="FCN3", shape=('','',1000), caption="", offset="(1.5,0,0)", to="(FCN2-east)", size=(1,1,18)),
    SoftMax(name="soft", shape=('','',1000) , offset="(1.5,0,0)", caption="Softmax", to="(FCN3-east)", size=(1,1,10)),
    
    Connection(of="pool1", to="conv21", label=''),
    Connection(of="pool2", to="conv31", label=''),
    Connection(of="pool3", to="conv41", label=''),
    Connection(of="pool4", to="conv51", label=''),
    Connection(of="pool5", to="FCN1", label=''), 
    Connection(of="FCN1", to="FCN2", label=''),
    Connection(of="FCN2", to="FCN3", label=''),
    Connection(of="FCN3", to="soft", label='')
    ]

if __name__ == '__main__':
    generate(arch, f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)
