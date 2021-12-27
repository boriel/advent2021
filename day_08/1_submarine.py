
total = 0
for line in open("input.txt"):
    left, right = (x.strip() for x in line.split('|'))
    right_codes = right.split()
    total += sum(len(x) in (2, 3, 4, 7) for x in right_codes)

print(total)
