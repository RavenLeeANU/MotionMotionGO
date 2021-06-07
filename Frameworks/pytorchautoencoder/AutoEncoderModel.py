import torch.nn as nn
import torch


class Autoencoder(nn.Module):

    def __init__(self,input_size = 256):
        super().__init__()

        self.encoder_hidden_layer = nn.Linear(in_features=input_size,out_features=128)
        self.encoder_output_layer = nn.Linear(in_features=128, out_features=64)

        self.decoder_hidden_layer = nn.Linear(in_features=64, out_features=128)
        self.decoder_output_layer = nn.Linear(in_features=128, out_features=input_size)

    def forward(self,features):
        layer_output = self.encoder_hidden_layer(features)
        layer_output = torch.relu(layer_output)
        layer_output = self.encoder_output_layer(layer_output)
        layer_output = torch.relu(layer_output)

        layer_output = self.decoder_hidden_layer(layer_output)
        layer_output = torch.relu(layer_output)
        layer_output = self.decoder_output_layer(layer_output)
        layer_output = torch.relu(layer_output)

        return layer_output