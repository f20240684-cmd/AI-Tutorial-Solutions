# Bayesian Networks and Autoregressive Language Models

This repository implements the laboratory on **Bayesian Networks and Autoregressive Language Models**.

The lab connects the chain rule of probability with a simple autoregressive language model and treats the first-order model as a small Bayesian network. It then asks for conditional probability tables, generation, testing, deterministic vs probabilistic generation and a second-order extension.

## Dataset

The supplied six-sentence dataset is used:

```text
the cat sat on the mat
the cat sat on the rug
the dog sat on the mat
the dog ran to the park
the cat ran to the park
the dog sat on the rug
```

Each sentence is converted to lower case and surrounded by `<START>` and `<END>`. This follows the laboratory specification.

## First-order model

The first-order model estimates:

```text
P(Xt | Xt-1)
```

The transition count is:

```text
C(current, next)
```

and the probability is:

```text
P(next | current) =
C(current, next) / sum_k C(current, k)
```

This is the conditional probability table described in the laboratory.

Run:

```bash
python first_order.py
```

The program prints probabilities for `the`, `cat`, `dog`, `sat` and `ran`, checks that each distribution sums to 1, prints greedy predictions and generates sampled sentences.

## Second-order model

The second-order model uses:

```text
P(Xt | Xt-2, Xt-1)
```

so the context is a pair of previous tokens.

Run:

```bash
python second_order.py
```

The laboratory describes the corresponding Bayesian-network structure as two previous variables pointing to the current variable.

## Greedy vs sampling

Greedy generation always chooses:

```text
argmax P(next | context)
```

Sampling chooses a token according to the probability distribution.

The lab asks for five examples of each mode and asks why sampling produces more variation.

## Probability test

For every context:

```text
sum_v P(v | context) = 1
```

The included test script checks this for both models.

```bash
python tests.py
```

If a total such as `0.87` appeared, it would indicate that the implementation had not constructed a valid normalized conditional distribution. The lab explicitly asks students to test this invariant.

## First-order vs second-order

| Feature | First-order | Second-order |
|---|---|---|
| Context | 1 previous token | 2 previous tokens |
| Distribution | `P(next \| current)` | `P(next \| previous 2)` |
| Context information | Smaller | Larger |
| Data requirement | Lower | Higher |
| Zero-count contexts | Fewer | More likely |

More context can improve prediction because the model can distinguish situations that have the same most recent word. At the same time, the number of possible contexts grows, so more training data is needed to estimate the table reliably. This is the trade-off highlighted by the laboratory.

## Connection to modern language models

The laboratory's important distinction is that an n-gram model and a modern language model are not comparable in expressive power. They share the same underlying probabilistic idea of predicting the next token conditional on previous tokens, but modern models use neural networks rather than small hand-built CPTs.

## Reflection

The LLM prompt is saved in `llm_prompt.txt`. I used the LLM to help with the implementation, but checked the transition-count logic and normalization independently.

The lab specifically requires submission of both implementations, selected CPTs, generated text, normalization results, answers to Questions 1–14 and a reflection on LLM use.

## Files

```text
first_order.py
second_order.py
tests.py
llm_prompt.txt
README.md
```
