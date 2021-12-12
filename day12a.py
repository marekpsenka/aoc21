import fileinput
from collections import defaultdict
from typing import List

input = map(str.rstrip, fileinput.input())

connected = defaultdict(list)

for line in input:
    fr, to = line.split("-")
    connected[fr].append(to)
    connected[to].append(fr)


def find_paths_step(paths: List[List[str]], path: List[str], this_cave: str) -> List[str]:
    if this_cave == "end":
        p = path.copy()
        p.append(this_cave)
        paths.append(p)
        return
    elif this_cave == "start":
        return
    elif this_cave.islower() and this_cave in path:
        return

    for nxt in connected[this_cave]:
        p = path.copy()
        p.append(this_cave)
        find_paths_step(paths, p, nxt)


def find_paths():
    paths = []
    path = ["start"]
    for nxt in connected["start"]:
        find_paths_step(paths, path, nxt)

    return paths


print(len(find_paths()))
