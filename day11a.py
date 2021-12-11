import fileinput

input = map(str.rstrip, fileinput.input())

octopuses = [[int(c) for c in line] for line in input]
lim_i = len(octopuses)
lim_j = len(octopuses[0])


def neighbors(i, j):
    if i == 0:
        if j == 0:
            return [(1, 0), (0, 1), (1, 1)]

        if j == lim_j - 1:
            return [(1, lim_j - 1), (0, lim_j - 2), (1, lim_j - 2)]

        return [(0, j - 1), (1, j), (0, j + 1), (1, j - 1), (1, j + 1)]

    if i == lim_i - 1:
        if j == lim_j - 1:
            return [(lim_i - 2, lim_j - 1), (lim_i - 1, lim_j - 2), (lim_i - 2, lim_j - 2)]

        if j == 0:
            return [(lim_i - 1, 1), (lim_i - 2, 0), (lim_i - 2, 1)]

        return [(lim_i - 1, j - 1), (lim_i - 2, j), (lim_i - 1, j + 1), (lim_i - 2, j - 1), (lim_i - 2, j + 1)]

    if j == 0:
        return [(i - 1, 0), (i, 1), (i + 1, 0), (i + 1, 1), (i - 1, 1)]

    if j == lim_j - 1:
        return [(i - 1, lim_j - 1), (i, lim_j - 2), (i + 1, lim_j - 1), (i - 1, lim_j - 2), (i + 1, lim_j - 2)]

    return [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j -1), (i - 1, j - 1)]


total_flashes = 0


def step():
    flashes = 0
    flashing = set()
    for i in range(lim_i):
        for j in range(lim_j):
            octopuses[i][j] += 1
            if octopuses[i][j] == 10:
                flashing.add((i, j))

    while len(flashing) > 0:
        to_flash = set()
        for i, j in flashing:
            for ni, nj in neighbors(i, j):
                octopuses[ni][nj] += 1
                if octopuses[ni][nj] == 10:
                    to_flash.add((ni, nj))
        flashes += len(flashing)
        flashing = to_flash

    for i in range(lim_i):
        for j in range(lim_j):
            if octopuses[i][j] > 9:
                octopuses[i][j] = 0

    return flashes


for _ in range(100):
    total_flashes += step()


print(total_flashes)
