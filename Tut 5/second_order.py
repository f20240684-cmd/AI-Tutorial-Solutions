from collections import defaultdict, Counter
import random

DATA = [
    "the cat sat on the mat",
    "the cat sat on the rug",
    "the dog sat on the mat",
    "the dog ran to the park",
    "the cat ran to the park",
    "the dog sat on the rug",
]


def prepare_data(sentences):
    result = []
    for sentence in sentences:
        words = sentence.lower().split()
        result.append(["<START>", "<START>"] + words + ["<END>"])
    return result


def build_model(sentences):
    counts = defaultdict(Counter)

    for sentence in sentences:
        for i in range(2, len(sentence)):
            context = (sentence[i - 2], sentence[i - 1])
            next_word = sentence[i]
            counts[context][next_word] += 1

    probabilities = {}

    for context, counter in counts.items():
        total = sum(counter.values())
        probabilities[context] = {
            word: count / total for word, count in counter.items()
        }

    return counts, probabilities


def most_probable(probabilities, context):
    if context not in probabilities:
        return None
    return max(probabilities[context], key=probabilities[context].get)


def sample_next(probabilities, context):
    if context not in probabilities:
        return None

    words = list(probabilities[context])
    weights = list(probabilities[context].values())
    return random.choices(words, weights=weights, k=1)[0]


def generate(probabilities, greedy=False, max_length=20):
    context = ("<START>", "<START>")
    sentence = []

    for _ in range(max_length):
        if greedy:
            next_word = most_probable(probabilities, context)
        else:
            next_word = sample_next(probabilities, context)

        if next_word is None or next_word == "<END>":
            break

        sentence.append(next_word)
        context = (context[1], next_word)

    return " ".join(sentence)


def main():
    random.seed(11)

    data = prepare_data(DATA)
    counts, probabilities = build_model(data)

    print("Second-order autoregressive model")
    print("-" * 50)

    for context in [("the", "cat"), ("the", "dog"), ("cat", "ran"),
                    ("dog", "sat"), ("sat", "on")]:
        print(f"\nP(next | {context})")
        for word, probability in sorted(probabilities.get(context, {}).items()):
            print(f"  {word:8s}: {probability:.3f}")

    print("\nProbability-normalisation test")
    for context, distribution in probabilities.items():
        print(f"{context}: {sum(distribution.values()):.3f}")

    print("\nSampling generation")
    for _ in range(10):
        print(generate(probabilities, greedy=False))


if __name__ == "__main__":
    main()
