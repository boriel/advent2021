ROLLS = 3


def sim_die(faces, start=0):
    counter = start

    def roll():
        nonlocal counter

        counter = counter % faces + 1
        return counter

    return roll


def roll_die(player, die, pos, scores):
    points = sum(die() for _ in range(ROLLS))
    pos[player] = (pos[player] - 1 + points) % 10 + 1
    scores[player] += pos[player]

    return scores[player]


pos = [int(x.strip()[-1]) for x in open("input.txt")]
scores = [0, 0]
player = 0
die = sim_die(100)
iter = 1

while roll_die(player, die, pos, scores) < 1000:
    player ^= 1
    iter += 1

print(iter * ROLLS * scores[player ^ 1])
