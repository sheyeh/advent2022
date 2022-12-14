import re

N = 9
stacks = []
for i in range(N):
    stacks.append([])
moves = False
with open('day5.txt', 'r') as f:
    for line in f:
        if line.startswith(" 1"):
            moves = True
            continue
        line = line.rstrip()
        if line == "":
            continue
        if not moves:
            line = line + " " * 30
            for i in range(N):
                c = line[1 + 4 * i]
                if c != ' ':
                    stacks[i].insert(0, c)
        else:
            num_to_move, move_from, move_to = [int(s) for s in re.split("move | from | to ", line)[1:]]
            stack_from = stacks[move_from - 1]
            stack_to = stacks[move_to - 1]
            stack_to += stack_from[len(stack_from) - num_to_move:]
            stack_from = stack_from[:len(stack_from) - num_to_move]
            stacks[move_from - 1] = stack_from

print("".join([stack[len(stack) - 1] for stack in stacks]))
