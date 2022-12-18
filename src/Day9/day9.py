import numpy

tail_pos = [[0, 0] for _ in range(9)]
# can make the head be the first knot, but leave it like this
head_pos = [0, 0]
MOVE = {
    "U": [1, 0],
    "D": [-1, 0],
    "L": [0, -1],
    "R": [0, 1]
}
covered_0 = {}
covered_8 = {}


def get_closer(x, y):
    return x if max(abs(x[i] - y[i]) for i in range(2)) <= 1 else \
        [x[0] - numpy.sign(x[0] - y[0]), x[1] - numpy.sign(x[1] - y[1])]


with open('day9.txt', 'r') as f:
    for line in f:
        direction, distance = line.split(" ")
        move = MOVE.get(direction)
        for d in range(int(distance)):
            head_pos[0] += move[0]
            head_pos[1] += move[1]
            tail_pos[0] = get_closer(tail_pos[0], head_pos)
            for k in range(1, 9):
                tail_pos[k] = get_closer(tail_pos[k], tail_pos[k - 1])
            covered_0[str(tail_pos[0])] = 1
            covered_8[str(tail_pos[8])] = 1

print("Part 1:", len(covered_0))
print("Part 2:", len(covered_8))
