def numMovesStones(a: int, b: int, c: int):
    a, b, c = sorted([a, b, c])
    answer = []
    if b - a == 2 or c - b == 2:
        answer.append(1)
    else:
        answer.append(min(1, abs(b - a - 1)) + min(1, abs(c - b - 1)))
    answer.append(abs(b - a - 1) + abs(c - b - 1))
    return answer
