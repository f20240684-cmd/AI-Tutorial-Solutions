import torch
import torch.nn as nn

torch.set_num_threads(1)

X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([0, 1, 1, 0])


class XORNet(nn.Module):
    def __init__(self, activation):
        super().__init__()
        self.hidden = nn.Linear(2, 2)
        self.output = nn.Linear(2, 1)

        if activation == "sigmoid":
            self.activation = nn.Sigmoid()
        elif activation == "tanh":
            self.activation = nn.Tanh()
        elif activation == "relu":
            self.activation = nn.ReLU()
        else:
            raise ValueError("Unknown activation")

    def forward(self, x):
        return self.output(self.activation(self.hidden(x)))


settings = {
    "sigmoid": 1,
    "tanh": 0,
    "relu": 2
}

for activation, seed in settings.items():
    torch.manual_seed(seed)
    model = XORNet(activation)
    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.1)

    early_gradient_norm = None

    for step in range(5000):
        logits = model(X)
        loss = loss_fn(logits, y.float().unsqueeze(1))

        optimizer.zero_grad()
        loss.backward()

        if step == 0:
            early_gradient_norm = model.hidden.weight.grad.norm().item()

        optimizer.step()

    with torch.no_grad():
        probabilities = torch.sigmoid(model(X)).squeeze()
        predictions = (probabilities >= 0.5).int()

    correct = int((predictions == y).sum().item())

    print(
        f"{activation:8s}  "
        f"loss={loss.item():.6f}  "
        f"correct={correct}/4  "
        f"early_grad={early_gradient_norm:.6f}"
    )
    print("  probabilities:", [round(p.item(), 4) for p in probabilities])
