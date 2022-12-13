priorities = 0
group_priority = 0
ord_a = ord('a')
ord_A = ord('A')
group = []
counter = 0


def priority(s):
    ord_s = ord(s)
    return ord_s - ((ord_a - 1) if ord_s > ord_a else (ord_A - 27))


with open('day3.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        group.append(line)
        counter += 1
        if counter == 3:
            badge = [s for s in group[0] if s in group[1] and s in group[2]][0]
            group_priority += priority(badge)
            group = []
            counter = 0
        L = int(len(line)/2)
        compartment_1 = line[:L]
        compartment_2 = line[L:]
        common = [s for s in compartment_1 if s in compartment_2][0]
        priorities += priority(common)

print("Part 1:", priorities)
print("Part 2:", group_priority)
