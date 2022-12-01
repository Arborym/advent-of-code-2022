# Part 1

with open("Day 1-input.txt", "r") as f:
    lines = f.readlines()
    total = 0
    max = 0
    for line in lines:
        if line != "\n":
            total += int(line)
        else:
            if total > max:
                max = total
            total = 0
    print(max)

# Part 2

with open("Day 1-input.txt", "r") as f:
    lines = f.readlines()
    total = 0
    max = 0
    max2 = 0
    max3 = 0
    for line in lines:
        if line != "\n":
            total += int(line)
        else:
            if total > max:
                max3 = max2
                max2 = max
                max = total
            elif total > max2:
                max3 = max2
                max2 = total
            elif total > max3:
                max3 = total
            total = 0
    print(max + max2 + max3)
