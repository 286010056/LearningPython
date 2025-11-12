# 【Pytorch】2024 Pytorch基础入门教程（完整详细版
# blog.csdn.net 北村南
import torch
from torch.utils.data import DataLoader
from torch.utils.data.dataset import TensorDataset

if __name__ == '__main__':
    # 自构建数据集
    dataset = TensorDataset(torch.arange(1, 41))
    print(dataset)
    dl = DataLoader(dataset,
                    batch_size=10,
                    shuffle=False,
                    num_workers=1,
                    drop_last=True)
    # 数据输出
    for batch in dl:
        print(batch)


