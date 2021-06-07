from model import Autoencoder
from dataloader import dataLoader
from tensorflow.keras import losses
import tensorflow.keras as keras
def train():
    train_set, test_set = dataLoader()
    latent_dim = 64
    autoencoder = Autoencoder(latent_dim)
    autoencoder.compile(optimizer='adam', loss=losses.MeanSquaredError())
    # auto loss
    autoencoder.fit(train_set, train_set,
                    epochs=10,
                    shuffle=True,
                    validation_data=(test_set, test_set))
    keras.models.save_model(model=autoencoder,filepath='./result/my_model')

if __name__ == "__main__":
    train()