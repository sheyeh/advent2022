import re
from monkey_classes import Monkey, Operation

THROW_TO = re.compile(".*monkey (\\d*)")
throw_true = {}
throw_false = {}
monkeys = {}
with open('day11.txt', 'r') as f:
    lines = f.readlines()
    m = 0
    while m * 7 < len(lines):
        mm = m * 7
        number = int(lines[mm].rstrip().split(" ")[1][:-1])
        queue = [int(i) for i in lines[mm + 1].split(":")[1].split(",")]
        operation_txt = lines[mm + 2].rstrip()[23:]
        operation = Operation(operation_txt)
        test = int(lines[mm + 3].split("by")[1])
        if_true = int(THROW_TO.match(lines[mm + 4]).group(1))
        if_false = int(THROW_TO.match(lines[mm + 5]).group(1))
        monkey = Monkey(number, queue, operation, test)
        monkeys[number] = monkey
        throw_true[number] = if_true
        throw_false[number] = if_false
        m += 1

for k, v in throw_true.items():
    monkeys[k].set_if_true(monkeys[v])

for k, v in throw_false.items():
    monkeys[k].set_if_false(monkeys[v])


for _ in range(20):
    for m in monkeys:
        monkeys[m].process()

inspections = [monkeys[m].inspections for m in monkeys]
m1 = max(inspections)
inspections.remove(m1)
m2 = max(inspections)
print(m1 * m2)
