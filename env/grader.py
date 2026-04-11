def grade(results):
    """
    results = list of reward.reason strings
    Example: ["correct", "wrong", "partial"]
    """

    if not results:
        return 0.0

    score = 0.0

    for r in results:
        if r == "correct":
            score += 1.0
        elif r == "partial":
            score += 0.5
        elif r == "wrong":
            score += 0.0
        else:
            score += 0.0  # safety fallback

    final_score = score / len(results)

    return round(final_score, 2)
