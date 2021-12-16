import fileinput
import math
from queue import PriorityQueue

input = map(str.rstrip, fileinput.input())

risk = [[int(c) for c in line] for line in input]
lim_i = len(risk)
lim_j = len(risk[0])


def neighbors(i, j):
    if i == 0:
        if j == 0:
            return [(1, 0), (0, 1)]

        if j == lim_j - 1:
            return [(1, lim_j - 1), (0, lim_j - 2)]

        return [(0, j - 1), (1, j), (0, j + 1)]

    if i == lim_i - 1:
        if j == lim_j - 1:
            return [(lim_i - 2, lim_j - 1), (lim_i - 1, lim_j - 2)]

        if j == 0:
            return [(lim_i - 1, 1), (lim_i - 2, 0)]

        return [(lim_i - 1, j - 1), (lim_i - 2, j), (lim_i - 1, j + 1)]

    if j == 0:
        return [(i - 1, 0), (i, 1), (i + 1, 0)]

    if j == lim_j - 1:
        return [(i - 1, lim_j - 1), (i, lim_j - 2), (i + 1, lim_j - 1)]

    return [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]


tentative = [[math.inf for _ in range(lim_j)] for _ in range(lim_i)]
tentative[0][0] = 0

q = PriorityQueue()
q.put((0, (0, 0)))

total_risk = None

while not q.empty():
    dist, pos = q.get()
    if pos == (lim_i - 1, lim_j - 1):
        total_risk = dist
        break

    if tentative[pos[0]][pos[1]] < dist:
        continue

    for ni, nj in neighbors(pos[0], pos[1]):
        cand = tentative[pos[0]][pos[1]] + risk[ni][nj]
        if cand < tentative[ni][nj]:
            tentative[ni][nj] = cand
            q.put((cand, (ni, nj)))

print(total_risk)
