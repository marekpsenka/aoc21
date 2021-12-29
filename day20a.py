import fileinput
from typing import Tuple, List, Dict

input = map(str.rstrip, fileinput.input())

string = ""

for line in input:
    if len(line) == 0:
        break
    string += line

assert len(string) == 512

Image = Dict[Tuple[int, int], str]

str_image = list(input)
image = dict()

for i in range(len(str_image)):
    for j in range(len(str_image[0])):
        image[(i, j)] = str_image[i][j]

bg = "."


def neighbors(i, j):
    return [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j),
            (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]


def extend(img: Image, bg: str) -> Image:
    ext = img.copy()
    for i, j in img:
        for n in neighbors(i, j):
            if n not in img:
                ext[n] = bg

    return ext


def from_binary(digits: List[int]) -> int:
    length = len(digits)
    acc = 0
    for i in range(length):
        acc += digits[i] * 2 ** (length - i - 1)

    return acc


def symbol_to_digit(symbol: str) -> int:
    if symbol == ".":
        return 0
    elif symbol == "#":
        return 1
    else:
        assert False


for step in range(2):
    extended = extend(image, bg)
    next_image = extended.copy()
    for i, j in extended:
        digits = [0] * 9
        for k, neighbor in enumerate(neighbors(i, j)):
            if neighbor not in extended:
                digits[k] = symbol_to_digit(bg)
            else:
                digits[k] = symbol_to_digit(extended[neighbor])
        next_image[(i, j)] = string[from_binary(digits)]
    image = next_image
    bg = string[from_binary([symbol_to_digit(bg)] * 9)]

print(sum(1 for v in image.values() if v == "#"))
