# Neural Models Lab

**Topic:** Learning, Depth, Activations, and Output Layers

This repository contains the Python implementations for the Neural Models laboratory exercise dated **August 7, 2026**.

The lab uses a very small XOR problem to study why a nonlinear hidden layer is needed, how the output layer and loss are chosen, how backpropagation appears in PyTorch, and how different initialization and activation choices affect learning. The later part extends the same input to a three-class problem. fileciteturn1file0L2-L14

## Requirements

- Python 3
- PyTorch
- NumPy

The lab states that CPU execution is sufficient. fileciteturn1file0L47-L54

Install:

```bash
pip install -r requirements.txt
```

## Files

```text
neural_models_lab_ex5/
│
├── xor_experiment.py
├── activation_experiment.py
├── symmetry_experiment.py
├── three_class.py
├── llm_prompt.txt
├── results.txt
├── requirements.txt
├── README.md
└── .gitignore
```

## 1. XOR experiment

The four training examples are:

| x1 | x2 | target |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

The baseline architecture required by the lab is:

```text
2 inputs -> 2 hidden units -> 1 output
```

The hidden layer uses `tanh`. The output is a logit and the loss is `BCEWithLogitsLoss`, which is the PyTorch form of the sigmoid + binary cross-entropy pairing discussed in the lab. fileciteturn1file0L86-L100

Run:

```bash
python xor_experiment.py
```

The program reports the initial/final loss, four probabilities, predicted labels, the number of correct predictions and a first-layer gradient tensor.

## 2. Symmetry experiment

The lab asks for an experiment where all weights are initialized to zero and the two hidden rows are inspected during training. fileciteturn1file0L149-L153

Run:

```bash
python symmetry_experiment.py
```

The hidden units remain symmetric because identical hidden units start with identical parameters and receive identical gradients.

## 3. Activation experiment

The lab asks for three runs using:

- sigmoid
- tanh
- ReLU

For each one, the final loss, number of correct predictions and early first-layer gradient norm are recorded. fileciteturn1file0L154-L164

Run:

```bash
python activation_experiment.py
```

The results should be interpreted only for this small XOR experiment. The lab specifically says not to treat the result as evidence that one activation is universally best. fileciteturn1file0L161-L168

## 4. Three-class extension

The original binary problem is changed to:

```text
Class 0 -> (0,0)
Class 1 -> (0,1) or (1,0)
Class 2 -> (1,1)
```

The output layer therefore contains three logits and the training loss is multiclass cross-entropy. This follows the extension specified in the lab. fileciteturn1file0L169-L190

Run:

```bash
python three_class.py
```

The program prints the softmax probabilities for all four inputs and checks that one probability vector sums to approximately 1.

## 5. Backpropagation

The main training loop follows:

```text
forward pass
      ↓
calculate loss
      ↓
zero gradients
      ↓
loss.backward()
      ↓
optimizer.step()
```

After `backward()`, a tensor such as:

```python
model.hidden.weight.grad
```

contains the gradient of the loss with respect to the first-layer weights.

This is the computational version of the chain-rule/backpropagation idea from the laboratory. The lab specifically asks for the gradient to be inspected after `backward()`. fileciteturn1file0L135-L148

## 6. Why XOR needs nonlinearity

A stack of affine layers without nonlinear hidden activations can be reduced to one affine transformation. Therefore, simply adding another affine layer does not solve the XOR representation problem. A nonlinear hidden layer changes the representation available to the network. fileciteturn1file0L29-L38

## 7. LLM usage

The laboratory asks for an LLM to be used as an engineering assistant and for the generated code to be inspected and tested rather than accepted automatically. fileciteturn1file0L106-L134

A copy of the prompt used for the implementation is in:

```text
llm_prompt.txt
```

The important point is that the architecture, data and validation checks were specified before generating the implementation.

## Main observations

1. A nonlinear hidden layer is needed to represent XOR.
2. A decrease in loss together with correct predictions is stronger evidence of learning than a nonzero gradient alone.
3. Identical hidden-unit initialization can preserve symmetry and prevent the hidden units from developing different features.
4. Different activations produce different gradient behaviour because their derivatives are different.
5. The output layer and loss function have to match the prediction task.
6. The three-class version uses three logits and softmax probabilities.
7. The LLM can help with implementation, but the experiments still need to be executed and checked independently.

## Running everything

```bash
python xor_experiment.py
python symmetry_experiment.py
python activation_experiment.py
python three_class.py
```

The file `results.txt` contains the outputs from the tested runs.

## Note

The code is intentionally kept small and direct because the purpose of the laboratory is to inspect the learning mechanism rather than build a large neural-network framework.
