cycle = 0
x = 1
power = 0
check_cycle = 20
CYCLE_DELTA = 40
screen = ""


def increase_cycle():
    global cycle, check_cycle, power, screen
    screen += "#" if abs(x - cycle % 40) <= 1 else "."
    cycle += 1
    if cycle == check_cycle:
        power += cycle * x
        check_cycle += CYCLE_DELTA


def increase_x(dx):
    global x
    x += dx


with open('day10.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line == "noop":
            increase_cycle()
        if line.startswith("addx"):
            increase_cycle()
            increase_cycle()
            delta_x = int(line.split(" ")[1])
            increase_x(delta_x)

print("Part 1:", power)
print("Part 2:")
for i in range(6):
    print(screen[i*40:(i+1)*40])
