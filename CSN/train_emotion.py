# train_emotion.py
import kagglehub
import pandas as pd
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os

# 1. 라벨 로드
df = kagglehub.load_dataset(
    "kagglehub.KaggleDatasetAdapter.PANDAS",
    "shuvoalok/raf-db-dataset",
    "train_labels.csv"
)

# 2. 데이터셋 클래스 정의
class RAFDBDataset(Dataset):
    def __init__(self, df, img_root, transform=None):
        self.df = df
        self.img_root = img_root
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img_path = os.path.join(self.img_root, row['image_name'])
        image = Image.open(img_path).convert('RGB')
        label = row['label'] - 1  # 0-based index
        if self.transform:
            image = self.transform(image)
        return image, label

# 3. 데이터 로더
transform = transforms.Compose([
    transforms.Resize((48, 48)),
    transforms.ToTensor(),
])

dataset = RAFDBDataset(df, img_root=r"C:\Users\YourName\.cache\kagglehub\...\train", transform=transform)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

# 4. 간단한 CNN
model = nn.Sequential(
    nn.Conv2d(3, 32, 3, padding=1),
    nn.ReLU(),
    nn.MaxPool2d(2),
    nn.Conv2d(32, 64, 3, padding=1),
    nn.ReLU(),
    nn.AdaptiveAvgPool2d((7,7)),
    nn.Flatten(),
    nn.Linear(64*7*7, 7)
)

# 5. 학습 루프 (간략)
optimizer = torch.optim.Adam(model.parameters())
criterion = nn.CrossEntropyLoss()

for epoch in range(10):
    for x, y in loader:
        out = model(x)
        loss = criterion(out, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# 6. 모델 저장
torch.save(model.state_dict(), "emotion_cnn.pth")