import torch
import torch.nn as nn

class BasicBlock(nn.Module):    # 기본블록정의
    # 기본 블록을 구성하는 총 정의
    def __init__(self, in_channels, out_channels, hidden_dim):
        #  nn.Module 클래스의 요소 상속
        super(BasicBlock, self).__init__()

        # 합성곱층 정의
        self.conv1 = nn.Conv2d(in_channels, hidden_dim, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(in_channels, hidden_dim, kernel_size=3, padding=1)
        self.relu = nn.ReLU()

        # stride는 커널의 이동 거리
        self.pool = nn.MaxPool2d(kernel_size=2, stride =2)

def forward(self,x) :
    x = self.conv1(x)
    x = self.relu(x)
    x = self.conv2(x)
    x = self.relu(x)
    x = self.pool(x)

    return x

# VGG_model
class CNN(nn.Module) :    # 기본블록정의
    def __init__(self, num_classes) :    # num_classes는 클래스 개수
        super(CNN, self).__init__()

        # 합성곱 기본 블록 정의
        self.block1 = BasicBlock(in_channels=3, out_channels=32, hidden_dim=16)
        self.block2 = BasicBlock(in_channels=32, out_channels=128, hidden_dim=64)
        self.block3 = BasicBlock(in_channels=128, out_channels=256, hidden_dim=128)

        # 분류기 정의
        self.fc1 = nn.Linear(in_features=4096, out_features=2048)
        self.fc2 = nn.Linear(in_features=2048, out_features=256)
        self.fc3 = nn.Linear(in_features=256, out_features=num_classes)

        # 분류기의 활성화 함수
        self.relu = nn.ReLU()

def forward(self,x) :
    x = self.block1(x)
    x = self.block2(x)
    x = self.block3(x)  # 출력 모양 : (-1,256,4,4)
    x = torch.flatten(x, start_dim=1)   # 2차원 특징 맵을 1차원으로

    x = self.fc1(x)
    x = self.relu(x)
    x = self.fc2(x)
    x = self.relu(x)
    x = self.fc3(x)

    return x

# ResNet_model_def
class ResNet(nn.Module):
    def __init__(self, num_classes=10):
        super(ResNet, self).__init__()

        self.b1 = BasicBlock(in_channels=3, out_channels=64)
        self.b2 = BasicBlock(in_channels=64, out_channels=128)
        self.b3 = BasicBlock(in_channels=128, out_channels=256)

        self.pool = nn.AvgPool2d(kernel_size=2, stride=2)

        self.fc1 = nn.Linear(in_features=4096, out_features=2048)
        self.fc2 = nn.Linear(in_features=2048, out_features=512)
        self.fc3 = nn.Linear(in_features=512, out_features=num_classes)

        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.b1(x)
        x = self.pool(x)
        x = self.b2(x)
        x = self.pool(x)
        x = self.b3(x)
        x = self.pool(x)

        x = torch.flatten(x, start_dim=1)

        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)

        return x