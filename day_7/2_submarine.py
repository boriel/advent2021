input = open("input.txt").read()
crabs = [int(x) for x in input.split(",")]

min_ = min(crabs)
max_ = max(crabs)

print(min(sum((lambda n: (n*n + n) // 2)(abs(x - pos)) for x in crabs) for pos in range(min_, max_ + 1)))
