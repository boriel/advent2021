WIN_SCORE = 21
CACHE = {}


def player_wins(universe):
    if universe in CACHE:
        return CACHE[universe]

    player, pos, scores = universe
    result = [0, 0]

    for i in [a + b + c for a in range(1, 4) for b in range(1, 4) for c in range(1, 4)]:
        new_pos = list(pos)
        new_pos[player] = (pos[player] - 1 + i) % 10 + 1
        new_scores = list(scores)
        new_scores[player] += new_pos[player]

        if new_scores[player] >= WIN_SCORE:
            result[player] += 1
            continue

        result = [a + b for a, b in zip(result, player_wins((player ^ 1, tuple(new_pos), tuple(new_scores))))]

    CACHE[universe] = result
    return result


print(player_wins((0, (5, 6), (0, 0))))
