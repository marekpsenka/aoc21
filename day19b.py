import fileinput
from typing import Dict, List, Tuple, Callable, Optional, Set
from itertools import combinations
from collections import defaultdict


class Vector():
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x},{self.y},{self.z})"

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))


def manhattan(p1: Vector, p2: Vector) -> int:
    return abs(p2.x - p1.x) + abs(p2.y - p1.y) + abs(p2.z - p1.z)


DistMap = Dict[int, List[Tuple[Vector, Vector]]]


def map_by_distances(beacons: Set[Vector]) -> DistMap:
    d = defaultdict(list)
    for b1, b2 in combinations(beacons, 2):
        dist = manhattan(b1, b2)
        d[dist].append((b1, b2))

    return d


input = map(str.rstrip, fileinput.input())

next(input)
all_beacons = []
beacons = set()

while True:
    try:
        line = next(input)
    except StopIteration:
        all_beacons.append(beacons)
        break

    if len(line) == 0:
        all_beacons.append(beacons)
        beacons = set()
        next(input)
    else:
        x, y, z = map(int, line.split(","))
        beacons.add(Vector(x, y, z))

maps = [map_by_distances(bs) for bs in all_beacons]

rotations = [
    lambda p: Vector(p.x, p.y, p.z), lambda p: Vector(-p.x, -p.y, p.z),
    lambda p: Vector(-p.x, p.y, -p.z), lambda p: Vector(p.x, -p.y, -p.z),
    lambda p: Vector(-p.x, -p.z, -p.y), lambda p: Vector(-p.x, p.z, p.y),
    lambda p: Vector(p.x, -p.z, p.y), lambda p: Vector(p.x, p.z, -p.y),
    lambda p: Vector(-p.y, -p.x, -p.z), lambda p: Vector(-p.y, p.x, p.z),
    lambda p: Vector(p.y, -p.x, p.z), lambda p: Vector(p.y, p.x, -p.z),
    lambda p: Vector(p.y, p.z, p.x), lambda p: Vector(-p.y, -p.z, p.x),
    lambda p: Vector(-p.y, p.z, -p.x), lambda p: Vector(p.y, -p.z, -p.x),
    lambda p: Vector(p.z, p.x, p.y), lambda p: Vector(-p.z, -p.x, p.y),
    lambda p: Vector(-p.z, p.x, -p.y), lambda p: Vector(p.z, -p.x, -p.y),
    lambda p: Vector(-p.z, -p.y, -p.x), lambda p: Vector(-p.z, p.y, p.x),
    lambda p: Vector(p.z, -p.y, p.x), lambda p: Vector(p.z, p.y, -p.x),
]

Rotation = Callable[[Vector], Vector]


def match(d1: DistMap, d2: DistMap, pts1: Set[Vector], pts2: Set[Vector]) -> \
        Optional[Tuple[Rotation, Vector]]:
    for dist in d1.keys() & d2.keys():
        for p1, p2 in d1[dist]:
            v = p2 - p1
            for q1, q2 in d2[dist]:
                w = q2 - q1
                for r in rotations:
                    rw = r(w)
                    if rw == v:
                        m = p1 - r(q1)
                        n = p2 - r(q2)
                    elif -rw == v:
                        m = p1 - r(q2)
                        n = p2 - r(q1)
                    else:
                        continue

                    if m != n:
                        continue

                    pts2_transformed = {r(p) + m for p in pts2}
                    if len(pts1.intersection(pts2_transformed)) >= 12:
                        return r, m

    return None


def merge(pts1: Set[Vector], pts2: Set[Vector], r: Rotation, m: Vector):
    return pts1.union({r(p) + m for p in pts2})


result_beacons = all_beacons[0]
result_distmap = maps[0]
scanner_positions = [Vector(0, 0, 0)]

del all_beacons[0]
del maps[0]

while len(all_beacons) > 0:
    for i in range(len(all_beacons)):
        res = match(result_distmap, maps[i], result_beacons, all_beacons[i])
        if res is not None:
            r, m = res
            scanner_positions.append(m)
            result_beacons = merge(result_beacons, all_beacons[i], r, m)
            result_distmap = map_by_distances(result_beacons)
            del all_beacons[i]
            del maps[i]
            break

max_distance = 0
for s1, s2 in combinations(scanner_positions, 2):
    dist = manhattan(s1, s2)
    if dist > max_distance:
        max_distance = dist

print(max_distance)
