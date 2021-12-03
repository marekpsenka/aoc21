import fileinput

input = map(str.rstrip, fileinput.input())
first = next(input)
length = len(first)

zeroCounts = [1 if c == '0' else 0 for c in first]
oneCounts = [1 if c == '1' else 0 for c in first]

for line in input:
    for i in range(length):
        if line[i] == '0':
            zeroCounts[i] += 1
        else:
            oneCounts[i] += 1

gamma_rate = 0
epsilon_rate = 0

for i in range(length):
    if zeroCounts[i] > oneCounts[i]:
        epsilon_rate += 2 ** ((length - 1) - i)
    else:
        gamma_rate += 2 ** ((length - 1) - i)

print (epsilon_rate * gamma_rate)
