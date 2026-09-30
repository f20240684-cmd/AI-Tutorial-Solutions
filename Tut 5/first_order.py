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
    tokenised = []
    for sentence in sentences:
        words = sentence.lower().split()
        tokenised.append(["<START>"] + words + ["<END>"])
    return tokenised


def build_model(sentences):
    transitions = defaultdict(Counter)

    for sentence in sentences:
        tokens = sentence
        for current, next_word in zip(tokens, tokens[1:]):
            transitions[current][next_word] += 1

    probabilities = {}

    for current, counts in transitions.items():
        total = sum(counts.values())
        probabilities[current] = {
            word: count / total for word, count in counts.items()
        }

    return transitions, probabilities


def most_probable(probabilities, current):
    if current not in probabilities:
        return None

    return max(probabilities[current], key=probabilities[current].get)


def sample_next(probabilities, current):
    if current not in probabilities:
        return None

    words = list(probabilities[current])
    weights = list(probabilities[current].values())
    return random.choices(words, weights=weights, k=1)[0]


def generate(probabilities, greedy=False, max_length=20):
    current = "<START>"
    sentence = []

    for _ in range(max_length):
        if greedy:
            next_word = most_probable(probabilities, current)
        else:
            next_word = sample_next(probabilities, current)

        if next_word is None or next_word == "<END>":
            break

        sentence.append(next_word)
        current = next_word

    return " ".join(sentence)


def print_table(probabilities, words):
    for word in words:
        print(f"\nP(next | {word})")
        if word not in probabilities:
            print("  no observed transition")
            continue

        for next_word, probability in sorted(probabilities[word].items()):
            print(f"  {next_word:8s}: {probability:.3f}")


def main():
    random.seed(7)

    data = prepare_data(DATA)
    transitions, probabilities = build_model(data)

    print("First-order autoregressive model")
    print("-" * 50)

    print_table(probabilities, ["the", "cat", "dog", "sat", "ran"])

    print("\nProbability-normalisation test")
    for word, distribution in probabilities.items():
        print(f"{word:8s}: {sum(distribution.values()):.3f}")

    print("\nMost probable next words")
    for word in ["the", "cat", "dog", "sat", "ran"]:
        print(f"{word:8s} -> {most_probable(probabilities, word)}")

    print("\nGreedy generation")
    for _ in range(5):
        print(generate(probabilities, greedy=True))

    print("\nSampling generation")
    for _ in range(20):
        print(generate(probabilities, greedy=False))


if __name__ == "__main__":
    main()
