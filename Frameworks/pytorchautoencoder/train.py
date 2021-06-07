import torch
import torch.nn as nn
import torch.optim as optim
import dataloader
from AutoEncoderModel import Autoencoder

def train(epochs = 100):

    train_loader, testloader = dataloader.prepare_data()

    #  use gpu if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # load it to the specified device, either gpu or cpu
    model = Autoencoder(input_size=784).to(device)

    # create an optimizer object
    # Adam optimizer with learning rate 1e-3
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    # mean-squared error loss
    criterion = nn.MSELoss()

    for epoch in range(epochs):

        loss = 0
        for batch_features, _ in train_loader:
            # reshape mini-batch data to [N, 784] matrix
            # load it to the active device
            batch_features = batch_features.view(-1, 784).to(device)

            # reset the gradients back to zero
            # PyTorch accumulates gradients on subsequent backward passes
            optimizer.zero_grad()

            # compute reconstructions
            outputs = model(batch_features)

            # compute training reconstruction loss
            train_loss = criterion(outputs, batch_features)

            # compute accumulated gradients
            train_loss.backward()

            # perform parameter update based on current gradients
            optimizer.step()

            # add the mini-batch training loss to epoch loss
            loss += train_loss.item()

        # compute the epoch training loss
        loss = loss / len(train_loader)

        # display the epoch training loss
        print("epoch : {}/{}, loss = {:.6f}".format(epoch + 1, epochs, loss))
        torch.save(model,'./result/poch-{}-model.pt'.format(epoch))

if __name__ == "__main__":
    train(10)

