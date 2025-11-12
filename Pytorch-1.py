# AI 学习笔记：用 PyTorch 训练一个简单的模型
# https://mp.weixin.qq.com/s/4uCKFj3IyBeMm1u8Z54eYg
import torch.nn as nn
class QuadrantClassifier(nn.Module):
    def __init__(self,input_size=2,hidden_size=64,output_size=4):
        self.network=nn.Sequential(
            nn.Linear(input_size,hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size,output_size)
        )

    def forward(self,x):
        return self.network(x)