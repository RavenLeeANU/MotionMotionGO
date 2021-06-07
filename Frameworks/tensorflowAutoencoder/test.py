import tensorflow as tf
from model import Autoencoder
from tensorflow import keras
import numpy as np
def test():

    model = keras.models.load_model('./result/my_model')
    # Train the model.
    test_input = np.random.random((1,28,28))

    result = model.predict(test_input)
    print(result)

if __name__ == "__main__":
    test()