data = [int(x) for x in open("input.txt")]
print(sum(sum(data[i: i + 3]) > sum(data[i - 1: i + 2]) for i in range(1, len(data) - 2)))
