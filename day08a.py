import fileinput

input = map(str.rstrip, fileinput.input())

count = 0

for line in input:
    patterns_str, digits_str = str.split(line, " | ")
    count += len([s for s in digits_str.split(" ") if len(s) in [2, 3, 4, 7]])

print(count)
