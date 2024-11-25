from plot_neural_net import *
import sys

# defined your arch
arch = [
    Conv("conv1", (512,512), 64, offset="(0,0,0)", to="(0,0,0)", height=64, depth=64, width=2 ),
    Pool("pool1", offset="(0,0,0)", to="(conv1-east)"),
    Conv("conv2", (128,128), 64, offset="(1,0,0)", to="(pool1-east)", height=32, depth=32, width=2 ),
    Connection( "pool1", "conv2"), 
    Pool("pool2", offset="(0,0,0)", to="(conv2-east)", height=28, depth=28, width=1),
    SoftMax("soft1", 10 ,"(3,0,0)", "(pool1-east)", caption="SOFT"  ),
    Connection("pool2", "soft1"),    
    Sum("sum1", offset="(1.5,0,0)", to="(soft1-east)", radius=2.5, opacity=0.6),
    Connection("soft1", "sum1"),
    ]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, '..' , namefile + '.tex' )

if __name__ == '__main__':
    main()
