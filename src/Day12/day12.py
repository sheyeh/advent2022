from dijkstra import Graph, DijkstraSPF

grid = []
S = None
E = None
with open('day12.txt', 'r') as f:
    i = 0
    for line in f:
        line = line.rstrip()
        j = line.find("S")
        if j >= 0:
            S = (i, j)
            line = line.replace("S", "a")
        j = line.find("E")
        if j >= 0:
            E = (i, j)
            line = line.replace("E", "z")
        grid.append(line)
        i += 1

N = len(grid)
M = len(grid[0])
graph = Graph()


def add_edge(i1, j1, i2, j2):
    if 0 <= i1 < N and 0 <= j1 < M and 0 <= i2 < N and 0 <= j2 < M:
        e1 = grid[i1][j1]
        e2 = grid[i2][j2]
        if ord(e2) - ord(e1) <= 1:
            graph.add_edge((i1, j1), (i2, j2), 1)


for i in range(N):
    for j in range(M):
        add_edge(i, j, i-1, j)
        add_edge(i, j, i+1, j)
        add_edge(i, j, i, j-1)
        add_edge(i, j, i, j+1)

d = DijkstraSPF(graph, S)
print(d.get_distance(E))
