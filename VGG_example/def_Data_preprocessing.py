import torch
import torch.nn as nn
import torch.cuda
import tqdm

from torchvision.datasets.cifar import CIFAR10
from torchvision.transforms import Compose, ToTensor
from torchvision.transforms import RandomHorizontalFlip, RandomCrop
from torchvision.transforms import Normalize
from torch.utils.data.dataloader import DataLoader

from torch.optim.adam import Adam

transforms = Compose([
    RandomCrop((32,32), padding=4), # 랜덤 크롭핑
    RandomHorizontalFlip(p=0.5),    # 랜덤 y축 대칭
    ToTensor(),
    Normalize(mean=(0.4914, 0.4822, 0.4465), std=(0.274, 0.243, 0.261))
])

# 데이터셋 정의
training_data = CIFAR10(root="./", train=True, download=True, transform=transforms)
test_data = CIFAR10(root="./", train=False, download=True, transform=transforms)

# 데이터로더 정의
train_loader = DataLoader(training_data, batch_size=32, shuffle=True)
train_loader = DataLoader(test_data, batch_size=32, shuffle=False)

#모델 정의하기
device = "cuda" if torch.cuda.is_available() else "cpu"

model = ResNet(num_classes=10)
model.to(device)

lr = 1e-4

optim = Adam(model.parameters(), lr=lr)

for epoch in range(30):
    iterator = tqdm.tqdm(train_loader)
    for data, label in iterator:
        # 최적화를 위해 기울기를 초기화
        optim.zero_grad()

        # 모델의 예측값
        preds = model(data.to(device))

        # 손실 계산 및 역전파
        loss = nn.CrossEntropyLoss()(preds, label.to(device))
        loss.backward()
        optim.step()

        iterator.set_description(f"epoch:{epoch+1} loss:{loss.item}")

torch.save(model.state_dict(), "ResNet.pth")
# 기억 배치농 프로바웃 캠