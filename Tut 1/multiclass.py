import torch

# Keep this tiny experiment quick on a CPU.
torch.set_num_threads(1)
import torch.nn as nn

# Class 0: both sensors inactive
# Class 1: sensors disagree
# Class 2: both sensors active
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([0, 1, 1, 2])

torch.manual_seed(42)


class ThreeClassNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(2, 2)
        self.output = nn.Linear(2, 3)

    def forward(self, x):
        x = torch.tanh(self.hidden(x))
        return self.output(x)


model = ThreeClassNet()
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

for step in range(3000):
    logits = model(X)
    loss = loss_fn(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    logits = model(X)
    probabilities = torch.softmax(logits, dim=1)
    predictions = probabilities.argmax(dim=1)

print("Three-class experiment")
print("-" * 40)
print(f"Final loss: {loss.item():.6f}")

for i in range(len(X)):
    probs = probabilities[i]
    print(
        f"{X[i].tolist()} -> "
        f"probabilities={[round(v.item(), 4) for v in probs]}, "
        f"predicted class={predictions[i].item()}"
    )

print("\nProbability sum for first example:",
      probabilities[0].sum().item())
