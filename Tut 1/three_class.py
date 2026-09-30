import torch
import torch.nn as nn

torch.set_num_threads(1)

# Class 0: (0,0)
# Class 1: (0,1) and (1,0)
# Class 2: (1,1)
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([0, 1, 1, 2])


class ThreeClassNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(2, 2)
        self.output = nn.Linear(2, 3)

    def forward(self, x):
        x = torch.tanh(self.hidden(x))
        return self.output(x)


torch.manual_seed(42)
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

print("Three-class extension")
print("-" * 45)
print(f"Final loss: {loss.item():.6f}")

for x, probability, prediction in zip(X, probabilities, predictions):
    values = [round(v.item(), 4) for v in probability]
    print(f"{x.tolist()} -> {values}, predicted class={prediction.item()}")

print("\nProbability sum for first example:",
      round(probabilities[0].sum().item(), 6))
