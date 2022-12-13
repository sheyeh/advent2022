priorities = 0
ord_a = ord('a')
ord_A = ord('A')
with open('day3.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        L = int(len(line)/2)
        compartment_1 = line[:L]
        compartment_2 = line[L:]
        ord_common = ord([s for s in compartment_1 if s in compartment_2][0])
        priority = ord_common - ((ord_a - 1) if ord_common > ord_a else (ord_A - 27))
        priorities += priority

print(priorities)
