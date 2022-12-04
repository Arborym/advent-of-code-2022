with open("Day 4-input.txt", "r") as f:
    s1, e1, s2, e2 = zip(
        *[
            [int(i) for i in line.replace(",", " ").replace("-", " ").split()]
            for line in f.read().splitlines()
        ]
    )
    print(
        "part 1:", sum((s1[i] - s2[i]) * (e1[i] - e2[i]) <= 0 for i in range(len(s1)))
    )
    print(
        "part 2:", sum((e2[i] - s1[i]) * (s2[i] - e1[i]) <= 0 for i in range(len(s1)))
    )
