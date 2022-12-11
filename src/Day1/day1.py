N = 3
top_N = [0] * N


def insert(c):
    global top_N
    for i in range(N):
        if c > top_N[i]:
            top_N.insert(i, c)
            top_N = top_N[:N]
            return


calories = 0
with open('day1.txt', 'r') as f:
    for line in f:
        if not line.rstrip():
            insert(calories)
            calories = 0
        else:
            calories += int(line.rstrip())

print("Part 1:", top_N[0])
print("Part 2:", sum(top_N))
