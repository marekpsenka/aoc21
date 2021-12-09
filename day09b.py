import fileinput

input = map(str.rstrip, fileinput.input())

floor = [[int(c) for c in line] for line in input]

local_minima = []

lim_i = len(floor)
lim_j = len(floor[0])


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


for i in range(lim_i):
    for j in range(lim_j):
        if all([floor[ni][nj] > floor[i][j] for ni, nj in neighbors(i, j)]):
            local_minima.append((i, j))


def find_basin_step(this, visited):
    visited.append(this)
    ti, tj = this
    for i, j in neighbors(ti, tj):
        fij = floor[i][j]
        if (i, j) not in visited and fij != 9 and fij >= floor[ti][tj]:
            find_basin_step((i, j), visited)


def find_basin(min):
    visited = []
    find_basin_step(min, visited)
    return visited


basins = []
for m in local_minima:
    basins.append(find_basin(m))

basins.sort(key=len)

print(len(basins[-1]) * len(basins[-2]) * len(basins[-3]))
