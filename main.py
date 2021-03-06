import torch, torchvision
import torch.nn.functional as F

import numpy as np
from matplotlib import pyplot as plt

from mnistmodel import Net

model = Net()
model.load_state_dict(torch.load('emnist.pt'))

tab = {}
dig = range(36)

for A in dig:
    for B in dig:
        tab[(A, B)] = torch.ones(1, 1, 28, 28) * 0.5

i = 0
while True:
    i += 1
    print(i)
    for A in dig:
        for B in dig:
            t = tab[(A, B)]
            t.requires_grad_()

            model.zero_grad()
            truth_1 = torch.tensor([A])
            guess_1 = model.forward(t.tanh())
            loss_1 = F.nll_loss(guess_1, truth_1)

            t_2 = t.flip(2).flip(3)
            truth_2 = torch.tensor([B])
            guess_2 = model.forward(t_2.tanh())
            loss_2 = F.nll_loss(guess_2, truth_2)

            loss = loss_1 + loss_2 + torch.norm(t, p=1) * 0.05
            loss.backward()
            tab[(A, B)] = t.detach() - t.grad.detach() * 0.1

            if i % 10 == 1:
                print(i, A, B, loss.item())
                np.save('emout-reg-hi/out-%d-%d.npz' % (A, B), t.detach().reshape(28, 28).numpy().transpose())
                plt.imsave('emout-reg-hi/out-%d-%d.png' % (A, B), t.detach().tanh().relu().reshape(28, 28).numpy().transpose(), cmap='binary')
