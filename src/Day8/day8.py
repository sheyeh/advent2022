forrest = []

with open('day8.txt', 'r') as f:
    for line in f:
        forrest.append([int(h) for h in line.rstrip()])

N = len(forrest)


def visible(i, j):
    if i in [0, N-1] or j in [0, N-1]:
        return 1
    return 1 if \
        forrest[i][j] > max(forrest[i][k] for k in range(j)) or \
        forrest[i][j] > max(forrest[i][k] for k in range(j + 1, N)) or \
        forrest[i][j] > max(forrest[k][j] for k in range(i)) or \
        forrest[i][j] > max(forrest[k][j] for k in range(i + 1, N)) \
        else 0


def seen(trees):
    length = len(trees)
    for i in range(1, length):
        if trees[i] >= trees[0]:
            return i
    return length - 1


def scenic_score(i, j):
    return seen([forrest[i][k] for k in range(j, N)]) * \
           seen([forrest[i][k] for k in range(j, -1, -1)]) * \
           seen([forrest[k][j] for k in range(i, N)]) * \
           seen([forrest[k][j] for k in range(i, -1, -1)])


count = sum(visible(i, j) for i in range(N) for j in range(N))
best_scenic_score = max(scenic_score(i, j) for i in range(N) for j in range(N))
print("Part 1:", count)
print("Part 2:", best_scenic_score)
