import torch
import torch.nn
import numpy as np

def test():

    model = torch.load('./result/poch-9-model.pt')
    input_tensor =np.random.rand(784)
    result = model(torch.Tensor(input_tensor))
    return result

if __name__ == "__main__":
    result =test()
    print(result)