import re


def fully_contained(a, b, c, d):
    return (int(a) <= int(c) and int(d) <= int(b)) or (int(c) <= int(a) and int(b) <= int(d))


def overlap(a, b, c, d):
    return not (int(b) < int(c) or int(d) < int(a))


contained = 0
overlaps = 0
with open('day4.txt', 'r') as f:
    for line in f:
        a, b, c, d = re.split("[,-]", line.rstrip())
        contained += 1 if fully_contained(a, b, c, d) else 0
        overlaps += 1 if overlap(a, b, c, d) else 0


print("Part 1:", contained)
print("Part 2:", overlaps)
