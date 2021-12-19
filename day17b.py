import fileinput

input = map(str.rstrip, fileinput.input())

line = next(input)

_, bounds_str = line.split(": ")
x_str, y_str = bounds_str.split(", ")
x_min, x_max = map(int, x_str[2:].split(".."))
y_min, y_max = map(int, y_str[2:].split(".."))


def first_ge_triangle(n: int) -> int:
    i = 1
    acc = 0
    while acc < n:
        acc += i
        i += 1

    return acc, i


_, v_x_min = first_ge_triangle(x_min)

hits = 0

for iv_x in range(v_x_min - 1, x_max + 1):
    for iv_y in range(y_min, -y_min + 1):
        x = 0
        y = 0
        v_x = iv_x
        v_y = iv_y
        while x <= x_max and y >= y_min:
            if x >= x_min and y <= y_max:
                hits += 1
                break
            x += v_x
            y += v_y
            v_x = max(0, v_x - 1)
            v_y -= 1

print(hits)
