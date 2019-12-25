import torch

x = torch.eye(3)

breakpoint()

for _ in range(5):
    x += 1

print(x)
