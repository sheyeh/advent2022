# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6

PLAYER_PLAYS_ROCK = "X"
PLAYER_PLAYS_PAPER = "Y"
PLAYER_PLAYS_SCISSORS = "Z"

result_p1 = {
    "A": {"X": ROCK + DRAW, "Y": PAPER + WIN, "Z": SCISSORS + LOSS},
    "B": {"X": ROCK + LOSS, "Y": PAPER + DRAW, "Z": SCISSORS + WIN},
    "C": {"X": ROCK + WIN, "Y": PAPER + LOSS, "Z": SCISSORS + DRAW}
}

players_play = {
    "A": {"X": PLAYER_PLAYS_SCISSORS, "Y": PLAYER_PLAYS_ROCK, "Z": PLAYER_PLAYS_PAPER},
    "B": {"X": PLAYER_PLAYS_ROCK, "Y": PLAYER_PLAYS_PAPER, "Z": PLAYER_PLAYS_SCISSORS},
    "C": {"X": PLAYER_PLAYS_PAPER, "Y": PLAYER_PLAYS_SCISSORS, "Z": PLAYER_PLAYS_ROCK}
}

score_p1 = 0
score_p2 = 0
with open('day2.txt', 'r') as f:
    for line in f:
        opponent, player = line.rstrip().split(" ")
        score_p1 += result_p1[opponent][player]
        score_p2 += result_p1[opponent][players_play[opponent][player]]

print("Part 1:", score_p1)
print("Part 2:", score_p2)
