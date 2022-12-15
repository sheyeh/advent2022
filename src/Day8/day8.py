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


count = sum(visible(i, j) for i in range(N) for j in range(N))
print(count)
