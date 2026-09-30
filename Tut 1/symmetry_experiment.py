import torch
import torch.nn as nn

torch.set_num_threads(1)

X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([[0.0], [1.0], [1.0], [0.0]])


class XORNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(2, 2)
        self.output = nn.Linear(2, 1)

    def forward(self, x):
        return self.output(torch.sigmoid(self.hidden(x)))


model = XORNet()

# The laboratory asks for all weights to be zero before training.
with torch.no_grad():
    for parameter in model.parameters():
        parameter.zero_()

loss_fn = nn.BCEWithLogitsLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.5)

print("Hidden weights before training:")
print(model.hidden.weight)

for step in range(5):
    logits = model(X)
    loss = loss_fn(logits, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(f"\nStep {step + 1}")
    print(model.hidden.weight)

print("\nThe hidden rows remain identical. With identical initial parameters,")
print("the hidden units receive identical gradients, so the symmetry is not broken.")
