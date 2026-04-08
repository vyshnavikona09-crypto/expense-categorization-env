def grade(results):
    correct = 0
    total = len(results)

    for r in results:
        if r == "correct":
            correct += 1

    return correct / total if total > 0 else 0.0
