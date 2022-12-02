def standardize(vals: list[str]) -> tuple[int, int]:
    ints = range(1, 4)
    return (ints["ABC".index(vals[0])], ints["XYZ".index(vals[1])])


def check_win(left: int, right: int) -> str:
    if right - left == 0:
        return "draw"
    if right - left in [-2, 1]:
        return "win"
    return "lose"


def score(left: int, right: int) -> int:
    return right + scores[res.index(check_win(left, right))]


scores = [0, 3, 6]
res = ["lose", "draw", "win"]

# Part 1

with open("Day 2-input.txt", "r") as f:
    data = [standardize(line.strip().split()) for line in f.readlines()]
    print(sum(score(left, right) for left, right in data))

# Part 2

with open("Day 2-input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        left, right = standardize(line.strip().split())
        find_choice = next(
            filter(
                lambda x, left=left, right=right: check_win(left, x) == res[right - 1],
                range(1, 4),
            )
        )
        total += score(left, find_choice)
    print(total)
