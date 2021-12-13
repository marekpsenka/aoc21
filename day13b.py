import fileinput
from typing import Set, Tuple

input = map(str.rstrip, fileinput.input())

dots = set()
coord_line = next(input)
while len(coord_line) > 0:
    x, y = map(int, coord_line.split(","))
    dots.add((x, y))
    coord_line = next(input)

folds = []
for fold_line in input:
    _, _, s = fold_line.split(" ")
    axis, pos = s.split("=")
    folds.append((axis, int(pos)))


def fold_horizontal(ds: Set[Tuple[int, int]], pos: int):
    nds = set()
    for x, y in ds:
        if y > pos:
            nds.add((x, pos - (y - pos)))
        else:
            nds.add((x, y))
    return nds


def fold_vertical(ds: Set[Tuple[int, int]], pos: int):
    nds = set()
    for x, y in ds:
        if x > pos:
            nds.add((pos - (x - pos), y))
        else:
            nds.add((x, y))
    return nds


def fold(ds: Set[Tuple[int, int]], fold: Tuple[str, int]):
    axis, pos = fold
    if axis == "x":
        return fold_vertical(ds, pos)
    elif axis == "y":
        return fold_horizontal(ds, pos)


def print_folded(ds: Set[Tuple[int, int]]):
    max_x, _ = max(ds, key=lambda d: d[0])
    _, max_y = max(ds, key=lambda d: d[1])
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if (j, i) in ds:
                print("#", end="")
            else:
                print(".", end="")
        print()


for f in folds:
    dots = fold(dots, f)

print_folded(dots)
