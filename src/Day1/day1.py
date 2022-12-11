max_calories = 0
calories = 0
with open('day1.txt', 'r') as f:
    for line in f:
        if not line.rstrip():
            max_calories = max(calories, max_calories)
            calories = 0
        else:
            calories += int(line.rstrip())

print(max_calories)
