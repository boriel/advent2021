data = [int(x) for x in open("input.txt")]
print(sum(x > data[i - 1] for i, x in enumerate(data) if i > 0))
