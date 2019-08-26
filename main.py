import torch, torchvision
import torch.nn.functional as F

import numpy as np
from matplotlib import pyplot as plt

from mnistmodel import Net

model = Net()
model.load_state_dict(torch.load('mnist.pt'))

#t = torch.tensor(np.random.randn(1, 1, 28, 28) * 0.1 + 0.5, dtype=torch.float)
t = torch.ones(1, 1, 28, 28) * 0.5

i = 0
while True:
    i += 1
    t.requires_grad_()

    A = 2
    B = 6

    model.zero_grad()
    truth_1 = torch.tensor([A])
    guess_1 = model.forward(t.tanh())
    loss_1 = F.nll_loss(guess_1, truth_1)

    t_2 = t.flip(2).flip(3)
    truth_2 = torch.tensor([B])
    guess_2 = model.forward(t_2.tanh())
    loss_2 = F.nll_loss(guess_2, truth_2)

    loss = loss_1 + loss_2# + torch.norm(t, p=1) * 0.001
    loss.backward()
    t = t.detach() - t.grad.detach() * 0.01

    if i % 1000 == 0:
        print(loss)
        print(guess_1)
        print(guess_2)
        plt.imsave('out-%d-%d-N.png' % (A, B), t.tanh().reshape(28, 28).numpy(), cmap='binary')
        plt.imsave('out-%d-%d-S.png' % (A, B), t_2.tanh().detach().reshape(28, 28).numpy(), cmap='binary')
