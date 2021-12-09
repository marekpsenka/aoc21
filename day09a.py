import fileinput

input = map(str.rstrip, fileinput.input())

floor = [[int(c) for c in line] for line in input]

sum_risk = 0

lim_i = len(floor)
lim_j = len(floor[0])

if (floor[0][0] < floor[1][0] and floor[0][0] < floor[0][1]):
    sum_risk += floor[0][0] + 1

if (floor[0][lim_j - 1] < floor[1][lim_j - 1] and floor[0][lim_j - 1] < floor[0][lim_j - 2]):
    sum_risk += floor[0][lim_j - 1] + 1

if (floor[lim_i - 1][lim_j - 1] < floor[lim_i - 2][lim_j - 1] and floor[lim_i - 1][lim_j - 1] < floor[lim_i - 1][lim_j - 2]):
    sum_risk += floor[lim_i - 1][lim_j - 1] + 1

if (floor[lim_i - 1][0] < floor[lim_i - 1][1] and floor[lim_i - 1][0] < floor[lim_i - 2][0]):
    sum_risk += floor[lim_i - 1][0] + 1

for j in range(1, lim_j - 1):
    val = floor[0][j]
    if val < floor[0][j - 1] and val < floor[1][j] and val < floor[0][j + 1]:
        sum_risk += val + 1

for j in range(1, lim_j - 1):
    val = floor[lim_i - 1][j]
    if val < floor[lim_i - 1][j - 1] and val < floor[lim_i - 2][j] and val < floor[lim_i - 1][j + 1]:
        sum_risk += val + 1

for i in range(1, lim_i - 1):
    val = floor[i][0]
    if val < floor[i - 1][0] and val < floor[i][1] and val < floor[i + 1][0]:
        sum_risk += val + 1

for i in range(1, lim_i - 1):
    val = floor[i][lim_j - 1]
    if val < floor[i - 1][lim_j - 1] and val < floor[i][lim_j - 2] and val < floor[i + 1][lim_j - 1]:
        sum_risk += val + 1

for i in range(1, lim_i - 1):
    for j in range(1, lim_j - 1):
        val = floor[i][j]
        if val < floor[i - 1][j] and val < floor[i][j + 1] and val < floor[i + 1][j] and val < floor[i][j - 1]:
            sum_risk += val + 1

print(sum_risk)
