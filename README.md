# plotnn

Modified from https://github.com/HarisIqbal88/PlotNeuralNet

1. install on your PC
    ```bash
    pip install -e /path/to/plotnn
    ```
2. write py file
   ```python
   # ./models/lenet.py
   from plotnn import *
    from pathlib import Path

    arch = [
        Input("../assets/cats.jpg",to="(-2,0,0)", height=6, width=6), 
        Conv("conv1", (28,28), 6, caption="CONV1", offset="(0,0,0)", to="(0,0,0)", height=30, width=30, depth=3),
        Pool("pool1", (14,14), 6, caption="POOL1", offset="(0,0,0)", to="(conv1-east)", height=20, width=20, depth=3, titlepos=-20),
        Conv("conv2", (10,10), 16,caption="CONV2",  offset="(2,0,0)", to="(pool1-east)", height=20, width=20, depth=3),
        Pool("pool2", (5,5), 16, caption="POOL2",offset="(0,0,0)", to="(conv2-east)", height=10, width=10, depth=3, titlepos=-20),
        FullyConnected("FCN1", n_filer=120, caption="FCN1", offset="(6,0,0)", depth=25),
        FullyConnected("FCN2", n_filer=84, caption="FCN2", offset="(7.5,0,0)", depth=18),
        SoftMax("soft", 10 ,"(9,0,0)", caption="SOFTMAX", depth=10),
        Connection("pool1", "conv2"),
        Connection("pool2", "FCN1"), 
        Connection("FCN1", "FCN2"),
        Connection("FCN2", "soft")
        ]

    if __name__ == '__main__':
        generate(arch, '.', f'./tmp/{Path(__file__).name.split(".")[0]}.tex', 14)
    ```
3. run plot command and get pdf file. make sue you installed LaTex on your computer.
   ```bash
   ./plotnn lenet
   ```
