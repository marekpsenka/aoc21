import fileinput
from typing import Tuple, List, Optional
from math import floor, ceil
from itertools import combinations


class Number():
    pass


class Regular(Number):
    def __init__(self, value: int) -> None:
        self.value = value

    def copy(self):
        return Regular(self.value)


class Pair(Number):
    def __init__(self, left: Number, right: Number) -> None:
        self.left = left
        self.right = right

    def copy(self):
        return Pair(self.left.copy(), self.right.copy())


def parse_sfn(s: str, pos: int) -> Tuple[Number, int]:
    pos += 1
    if s[pos] == "[":
        left, pos = parse_sfn(s, pos)
    else:
        left = Regular(int(s[pos]))
        pos += 1

    assert s[pos] == ","
    pos += 1

    if s[pos] == "[":
        right, pos = parse_sfn(s, pos)
    else:
        right = Regular(int(s[pos]))
        pos += 1

    return Pair(left, right), pos + 1


def magnitude(n: Number) -> int:
    if type(n) is Regular:
        return n.value
    elif type(n) is Pair:
        return 3 * magnitude(n.left) + 2 * magnitude(n.right)


def path_to_exploding_pair_step(p: Number, path: List[Pair]) -> Optional[List[Pair]]:
    if type(p) is Regular:
        return None
    elif type(p) is Pair:
        path_copy = path.copy()
        path_copy.append(p)
        if len(path) == 4:
            return path_copy
        lr = path_to_exploding_pair_step(p.left, path_copy)
        if lr is None:
            return path_to_exploding_pair_step(p.right, path_copy)
        return lr


def path_to_exploding_pair(p: Pair) -> Optional[List[Pair]]:
    path = []
    return path_to_exploding_pair_step(p, path)


def explode_by_path(path: List[Pair]) -> None:
    assert type(path[-1].left) is Regular
    assert type(path[-1].right) is Regular

    for child, parent in zip(reversed(path), reversed(path[:-1])):
        if child is parent.left:
            continue
        node = parent.left
        while type(node) is not Regular:
            node = node.right

        node.value += path[-1].left.value
        break

    for child, parent in zip(reversed(path), reversed(path[:-1])):
        if child is parent.right:
            continue
        node = parent.right
        while type(node) is not Regular:
            node = node.left

        node.value += path[-1].right.value
        break

    if path[-1] is path[-2].left:
        path[-2].left = Regular(0)
    elif path[-1] is path[-2].right:
        path[-2].right = Regular(0)
    else:
        assert False


def path_to_splitting_number_step(p: Number, path: List[Number]) -> Optional[List[Number]]:
    path_copy = path.copy()
    path_copy.append(p)
    if type(p) is Regular:
        if p.value >= 10:
            return path_copy
        else:
            return None
    elif type(p) is Pair:
        lr = path_to_splitting_number_step(p.left, path_copy)
        if lr is None:
            return path_to_splitting_number_step(p.right, path_copy)
        return lr


def path_to_splitting_number(p: Number) -> Optional[List[Number]]:
    path = []
    return path_to_splitting_number_step(p, path)


def split_by_path(path: List[Number]) -> None:
    assert type(path[-1]) is Regular
    assert type(path[-2]) is Pair
    if path[-1] is path[-2].left:
        path[-2].left = Pair(Regular(floor(path[-1].value / 2)),
                             Regular(ceil(path[-1].value / 2)))
    elif path[-1] is path[-2].right:
        path[-2].right = Pair(Regular(floor(path[-1].value / 2)),
                              Regular(ceil(path[-1].value / 2)))
    else:
        assert False


def reduce(sfn: Pair) -> None:
    while True:
        path_to_exploding = path_to_exploding_pair(sfn)
        if path_to_exploding is not None:
            explode_by_path(path_to_exploding)
        else:
            path_to_splitting = path_to_splitting_number(sfn)
            if path_to_splitting is None:
                break

            split_by_path(path_to_splitting)


def add(sfn1, sfn2):
    sfn = Pair(sfn1, sfn2)
    reduce(sfn)
    return sfn


input = map(str.rstrip, fileinput.input())
sfns = []

for line in input:
    sfn, pos = parse_sfn(line, 0)
    sfns.append(sfn)

max = 0

for sfn1, sfn2 in combinations(sfns, 2):
    mag = magnitude(add(sfn1.copy(), sfn2.copy()))
    if mag > max:
        max = mag
    mag = magnitude(add(sfn2.copy(), sfn1.copy()))
    if mag > max:
        max = mag

print(max)
