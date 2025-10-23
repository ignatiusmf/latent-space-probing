from rich import print as pprint
import torch
import torch.nn.functional as F
from matplotlib import pyplot as plt
def show_sgm(Xc, W):
  XcW = Xc @ W # (N, n) @ (n, k) -> (N, k)
  XcWWT = XcW @ W.T  # (N, k) @ (k, n) -> (N, n)
  plt.figure(figsize=(5, 4))

  loss = F.mse_loss(Xc, XcWWT)

  plt.subplot(1, 3, 1)
  plt.matshow(W.detach(), fignum=False, vmin=-1, vmax=1)
  plt.title('W (weights)')

  # plt.subplot(1, 3, 2)
  # plt.matshow(Xc.detach(), fignum=False, vmin=-2, vmax=2)
  # plt.title('Xc (centered data)')

  # plt.subplot(1, 3, 3)
  # plt.matshow(XcWWT.detach(), fignum=False, vmin=-2, vmax=2)
  # plt.title('XcWWT (reconstruction)')

  plt.subplot(1, 3, 2)
  plt.matshow((Xc-XcWWT).detach(), fignum=False, vmin=-0.5, vmax=0.5)
  plt.title(f'Xc - XcWWT, loss={loss.item():.1e}')

  plt.tight_layout()
  plt.show()









N = 10 
n = 5  
k = 5

X = torch.randn(N, n)
Xc = X - X.mean(0, keepdim=True)
W = torch.randn(n, k, requires_grad=True)

show_sgm(Xc, W)


steps = 10000

opt = torch.optim.Adam([W], lr=1e-2)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=steps)  

losses = []
for step in range(steps):
    XcW   = Xc @ W          # (N, k)
    XcWWT = XcW @ W.T       # (N, n)
    loss  = F.mse_loss(XcWWT, Xc)
    losses.append(loss.log10().item())

    opt.zero_grad()
    loss.backward()

    opt.step()
    scheduler.step()
    

    if step % (steps // 10) == 0 or step == steps-1:
        current_lr = opt.param_groups[0]['lr']  # More robust way to get current LR
        print(f"step {step:4d}  loss {loss.item():.16f}  lr {current_lr:.16f}")
        # print(step)


plt.plot(losses)
plt.show()
show_sgm(Xc, W)