import torch
import torch.optim as optim


def f(in_x, target):
    return (in_x - target).pow(2)


x = torch.tensor(5.0, requires_grad=True)
target = torch.tensor(1.0)

# lr stands for learning rate, i.e. stepsize.
optimizer = optim.Adam([x], lr=1.0)

breakpoint()

for step_idx in range(250):
    optimizer.zero_grad()
    y = f(x, target)
    y.backward()
    optimizer.step()

print(x)
