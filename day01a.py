import fileinput

acc = 0
input = fileinput.input()
last = int(next(input))

for line in input:
    if int(line) > last:
        acc += 1

    last = int(line)

print(acc)