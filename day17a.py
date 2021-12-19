import fileinput

input = map(str.rstrip, fileinput.input())

line = next(input)

_, bounds_str = line.split(": ")
x_str, y_str = bounds_str.split(", ")
x_min, x_max = map(int, x_str[2:].split(".."))
y_min, y_max = map(int, y_str[2:].split(".."))


print(((-y_min) * (-y_min - 1)) // 2)
