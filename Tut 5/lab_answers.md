# Lab Answers

## Question 1

The chain-rule decomposition is useful because it turns the probability of a whole sentence into a sequence of next-token conditional probabilities. Text can therefore be generated one token at a time.

## Question 2

The first-order network assumes:

```text
P(Xt | X1, ..., Xt-1) = P(Xt | Xt-1)
```

So the next word depends only on the immediately preceding word.

## Question 3

For the supplied data:

```text
P(next | the):
cat = 0.25
dog = 0.25
mat = 0.1667
rug = 0.1667
park = 0.1667

P(next | cat):
sat = 0.6667
ran = 0.3333

P(next | dog):
sat = 0.6667
ran = 0.3333

P(next | sat):
on = 1.0

P(next | ran):
to = 1.0
```

Zero-probability transitions are all transitions that were not observed in the training data.

## Question 4

Transition counts are stored in the `defaultdict(Counter)` named `transitions` in `first_order.py`.

## Question 5

The conditional probability is computed when each transition count is divided by the total count for the current word.

## Question 6

The program supports both:
- greedy selection using the maximum probability;
- sampling using the probability distribution.

Greedy generation is deterministic for a fixed model. Sampling can produce different sentences.

## Question 7

If a word has no observed outgoing transition, the program returns `None` and stops generation.

## Question 8

A total such as `0.87` means the conditional probabilities have not been normalized correctly, because a complete conditional distribution should sum to approximately 1.

## Question 9

No. A probability model only uses the probabilities estimated from its training data. Human expectations can use broader linguistic knowledge that is not represented by the small model.

## Question 10

Sampling produces more variation because it does not always choose the maximum-probability word. Greedy generation repeatedly makes the same locally best choice and can get stuck in repetitive patterns.

## Question 11

A second-order model:
1. has two previous tokens as parents of the current token;
2. stores counts for token pairs rather than single tokens;
3. uses more context for prediction;
4. generally needs more data because there are more possible contexts.

## Question 12

More context can distinguish situations that look identical under a first-order model. However, increasing context also increases the number of possible conditional contexts, so more training data is required to estimate probabilities reliably.

## Question 13

A precise probabilistic specification is preferable because it tells the LLM exactly what model it must implement. This makes it easier to inspect the representation, test invariants and detect an implementation that does something different from the intended model.

## Question 14

Thinking of the model as a Bayesian network gives:
- an explicit representation of dependencies;
- a factorisation of the joint distribution;
- a clear interpretation of conditional probabilities;
- a principled generation procedure;
- a way to reason about the independence assumptions.
