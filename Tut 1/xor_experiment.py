import torch
import torch.nn as nn

torch.set_num_threads(1)

X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])

y = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])


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
        hidden = self.activation(self.hidden(x))
        return self.output(hidden)


def train(seed=0, activation="tanh", steps=5000, lr=0.1):
    torch.manual_seed(seed)

    model = XORNet(activation)
    loss_fn = nn.BCEWithLogitsLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    initial_loss = None
    early_gradient = None

    for step in range(steps):
        logits = model(X)
        loss = loss_fn(logits, y)

        if step == 0:
            initial_loss = loss.item()

        optimizer.zero_grad()
        loss.backward()

        if step == 0:
            early_gradient = model.hidden.weight.grad.detach().clone()

        optimizer.step()

    with torch.no_grad():
        probabilities = torch.sigmoid(model(X)).squeeze()
        predictions = (probabilities >= 0.5).int()

    return model, initial_loss, loss.item(), probabilities, predictions, early_gradient


if __name__ == "__main__":
    model, initial_loss, final_loss, probabilities, predictions, gradient = train()

    print("XOR Neural Network")
    print("-" * 45)
    print("Architecture: 2 inputs -> 2 hidden units -> 1 output")
    print("Hidden activation: tanh")
    print("Loss: BCEWithLogitsLoss")
    print()
    print(f"Initial loss: {initial_loss:.6f}")
    print(f"Final loss:   {final_loss:.6f}")
    print(f"Early ||gradient W1||: {gradient.norm().item():.6f}")
    print()
    print("Input       Probability    Prediction")

    for x, probability, prediction in zip(X, probabilities, predictions):
        print(
            f"{x.tolist()}     "
            f"{probability.item():.6f}       "
            f"{prediction.item()}"
        )

    print(f"\nCorrect predictions: {(predictions == y.squeeze().int()).sum().item()}/4")

    # This is the gradient tensor requested in the lab.
    print("\nFirst-layer gradient tensor from the first backward pass:")
    print(gradient)
