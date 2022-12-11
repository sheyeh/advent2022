# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6

result = {
    "A": {"X": ROCK + DRAW, "Y": PAPER + WIN, "Z": SCISSORS + LOSS},
    "B": {"X": ROCK + LOSS, "Y": PAPER + DRAW, "Z": SCISSORS + WIN},
    "C": {"X": ROCK + WIN, "Y": PAPER + LOSS, "Z": SCISSORS + DRAW}
}

score = 0
with open('day2.txt', 'r') as f:
    for line in f:
        opponent, player = line.rstrip().split(" ")
        score += result[opponent][player]

print("Part 1:", score)
