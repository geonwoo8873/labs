import torch
print("torch:", torch.__version__)
print("hip:", torch.version.hip)
print("cuda.is_available:", torch.cuda.is_available())

try:
    x = torch.tensor([1.0, 2.0, 3.0], device="cuda")
    y = x * 2
    print("GPU tensor ok:", y, y.device)
except Exception as e:
    print("GPU tensor failed:", repr(e))