input = open("input.txt", "r").read()
num_generations = 80
current = [0] * 9
next = [0] * 9

for i in input.split(","):
    current[int(i)] += 1

for i in range(num_generations):
    for j in range(8):
        next[j] = current[j+1]

    next[8] = current[0]
    next[6] += current[0]
    current = list(next)


print(sum(current))
