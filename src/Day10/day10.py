cycle = 0
x = 1
power = 0
check_cycle = 20
CYCLE_DELTA = 40


def increase_cycle():
    global cycle, check_cycle, power
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

print(power)
