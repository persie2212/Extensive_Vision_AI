from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms

class Net(nn.Module):
    def __init__(self, input_ch=3):
        super(Net, self).__init__()
        self.input_ch = input_ch

        # Input/Prep Block
        self.convblock1 = nn.Sequential(
            nn.Conv2d(in_channels=input_ch, out_channels=64, kernel_size=(
                3, 3), padding=1, stride=1, bias=False),
            nn.BatchNorm2d(64),
            nn.ReLU()
        )  # input =3, output=64 channels
        # Layer 1
        self.convblock2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=(
                3, 3), padding=1, stride=1, bias=False),
            nn.MaxPool2d(2, 2),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )

        self.resblock1 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=(
                3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=(
                3, 3), padding=1, bias=False),
            nn.BatchNorm2d(128),
            nn.ReLU()
        )
        # Layer 2
        self.convblock3 = nn.Sequential(
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=(
                3, 3), padding=1, bias=False),
            nn.MaxPool2d(2, 2),
            nn.BatchNorm2d(256),
            nn.ReLU()
        )
        # Layer 3
        self.convblock4 = nn.Sequential(
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=(
                3, 3), padding=1, stride=1, bias=False),
            nn.MaxPool2d(2, 2),
            nn.BatchNorm2d(512),
            nn.ReLU()
        )

        self.resblock2 = nn.Sequential(
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=(
                3, 3), padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU(),
            nn.Conv2d(in_channels=512, out_channels=512, kernel_size=(
                3, 3), padding=1, bias=False),
            nn.BatchNorm2d(512),
            nn.ReLU()
        )

        self.pool1 = nn.MaxPool2d(4, 4)

        self.fc = nn.Sequential(nn.Linear(512, 10))

    def forward(self, x):
        x = self.convblock1(x)  # PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]
        X = self.convblock2(x)
        R1 = self.resblock1(
            X)  # Layer1 -X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k] R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] Add(X, R1)
        x = X + R1
        x = self.convblock3(x)
        X = self.convblock4(x)
        R2 = self.resblock2(X)
        x = X + R2
        x = self.pool1(x)
        #  x4 = self.pool1(torch.cat((x, x2, x3), dim=1))
        x = x.view(x.size(0), -1)  # 10
        x = self.fc(x)
        return F.log_softmax(x, dim=1)