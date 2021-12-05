import fileinput

input = map(str.rstrip, fileinput.input())

m = dict()

for line in input:
    [bs, es] = line.split(" -> ")
    (x1, y1) = tuple(map(int, bs.split(",")))
    (x2, y2) = tuple(map(int, es.split(",")))
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            if (not (x1, i) in m):
                m[(x1, i)] = 1
            else:
                m[(x1, i)] = m[(x1, i)] + 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            if (not (i, y1) in m):
                m[(i, y1)] = 1
            else:
                m[(i, y1)] = m[(i, y1)] + 1
    else:
        vy = y2 - y1
        vx = x2 - x1
        dy = - 1
        if vy > 0:
            dy = 1
        dx = - 1
        if vx > 0:
            dx = 1
        for i in range(abs(vy) + 1):
            p = (x1 + i * dx, y1 + i * dy)
            if (not p in m):
                m[p] = 1
            else:
                m[p] = m[p] + 1

count = 0

for v in m.values():
    if v > 1:
        count += 1

print(count)