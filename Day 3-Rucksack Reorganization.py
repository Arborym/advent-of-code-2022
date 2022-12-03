# Part 1

print(
    sum(
        ord(item) - 96 if item.islower() else ord(item) - 38
        for items in open("Day 3-input.txt", "r")
        for item in set(items[: len(items) // 2]) & set(items[len(items) // 2 :])
    )
)

# Part 2

print(
    sum(
        i + 1
        for l in range(0, len(open("Day 3-input.txt", "r").readlines()), 3)
        for i in range(len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        if all(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"[i] in line
            for line in open("Day 3-input.txt", "r").readlines()[l : l + 3]
        )
    )
)
