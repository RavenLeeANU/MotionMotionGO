from tensorflow.keras.datasets import fashion_mnist

def dataLoader():
    (x_train, _), (x_test, _) = fashion_mnist.load_data()

    x_train = x_train.astype('float32') / 255.
    x_test = x_test.astype('float32') / 255.

    print(x_train.shape)
    print(x_test.shape)
    return x_train,x_test