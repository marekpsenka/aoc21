import fileinput

input = map(str.rstrip, fileinput.input())

fish = [int(s) for s in next(input).split(",")]

for j in range(80):
    for i in range(len(fish)):
        if (fish[i] == 0):
            fish[i] = 6
            fish.append(8)
        else:
            fish[i] -= 1

print(len(fish))