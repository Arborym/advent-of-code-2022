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
    max_list = [0, 0, 0]
    for line in lines:
        if line != "\n":
            total += int(line)
        else:
            if total > max_list[0]:
                max_list[2] = max_list[1]
                max_list[1] = max_list[0]
                max_list[0] = total
            elif total > max_list[1]:
                max_list[2] = max_list[1]
                max_list[1] = total
            elif total > max_list[2]:
                max_list[2] = total
            total = 0
    print(max_list[0] + max_list[1] + max_list[2])
