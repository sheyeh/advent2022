# A, X: Rock
# B, Y: Paper
# C, Z: Scissors

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSS = 0
DRAW = 3
WIN = 6

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

PLAYER_ROCK = "X"
PLAYER_PAPER = "Y"
PLAYER_SCISSORS = "Z"

result_p1 = {
    OPPONENT_ROCK: {
        PLAYER_ROCK: ROCK + DRAW,
        PLAYER_PAPER: PAPER + WIN,
        PLAYER_SCISSORS: SCISSORS + LOSS
    },
    OPPONENT_PAPER: {
        PLAYER_ROCK: ROCK + LOSS,
        PLAYER_PAPER: PAPER + DRAW,
        PLAYER_SCISSORS: SCISSORS + WIN
    },
    OPPONENT_SCISSORS: {
        PLAYER_ROCK: ROCK + WIN,
        PLAYER_PAPER: PAPER + LOSS,
        PLAYER_SCISSORS: SCISSORS + DRAW
    }
}

NEED_TO_LOSE = "X"
NEED_TO_DRAW = "Y"
NEED_TO_WIN = "Z"

players_play = {
    OPPONENT_ROCK: {
        NEED_TO_LOSE: PLAYER_SCISSORS,
        NEED_TO_DRAW: PLAYER_ROCK,
        NEED_TO_WIN: PLAYER_PAPER
    },
    OPPONENT_PAPER: {
        NEED_TO_LOSE: PLAYER_ROCK,
        NEED_TO_DRAW: PLAYER_PAPER,
        NEED_TO_WIN: PLAYER_SCISSORS
    },
    OPPONENT_SCISSORS: {
        NEED_TO_LOSE: PLAYER_PAPER,
        NEED_TO_DRAW: PLAYER_SCISSORS,
        NEED_TO_WIN: PLAYER_ROCK
    }
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
