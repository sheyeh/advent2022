with open('day6.txt', 'r') as f:
    for line in f:
        stream = line


def marker(marker_length):
    for i in range(marker_length, len(stream)):
        header = stream[i - marker_length:i]
        if len(set(header)) == marker_length:
            return i
    return None


print("Part 1:", marker(4))
print("Part 2:", marker(14))
