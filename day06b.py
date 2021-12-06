import fileinput

input = map(str.rstrip, fileinput.input())

ages = [int(s) for s in next(input).split(",")]

gen = [0 for i in range(9)]

for a in ages:
    gen[a] += 1

for i in range(256):
    next_gen = [0 for i in range(9)]
    for j in range(9):
        if j == 0:
            next_gen[6] += gen[0]
            next_gen[8] += gen[0]
        else:
            next_gen[j - 1] += gen[j]
    gen = next_gen

print(sum(gen))


