def winner(names: list[str], scores: list[float]) -> str:
    best_index = 0

    for i in range(1, len(scores)):
        if scores[i] > scores[best_index]:
            best_index = i

    return names[best_index]


def average(scores: list[float]) -> float:
    if len(scores) == 0:
        return 0.0

    return round(sum(scores) / len(scores), 2)


def ranking(names: list[str], scores: list[float]) -> list[str]:
    results = sorted(zip(scores, names), key=lambda item: item[0], reverse=True)

    return [name for score, name in results]