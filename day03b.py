import fileinput

input = list(map(str.rstrip, fileinput.input()))
length = len(input[0])

def counts(l, pos):
    zeros = 0
    ones = 0
    for s in l:
        if s[pos] == '0':
            zeros += 1
        else:
            ones += 1

    return zeros, ones

def find_oxy(l):
    pos = 0
    while (len(l) > 1):
        zeros, ones = counts(l, pos)
        if zeros > ones:
            l = [s for s in l if s[pos] == '0']
        elif ones > zeros:
            l = [s for s in l if s[pos] == '1']
        else:
            l = [s for s in l if s[pos] == '1']
        pos += 1
    return l[0]

def find_co2(l):
    pos = 0
    while (len(l) > 1):
        zeros, ones = counts(l, pos)
        if zeros > ones:
            l = [s for s in l if s[pos] == '1']
        elif ones > zeros:
            l = [s for s in l if s[pos] == '0']
        else:
            l = [s for s in l if s[pos] == '0']
        pos += 1
    return l[0]

def to_binary(s : str) -> int:
    n = 0
    l = len(s)
    for i in range(l):
        if s[i] == '1':
            n += 2 ** ((l - 1) - i)

    return n

oxy = to_binary(find_oxy(input.copy()))
co2 = to_binary(find_co2(input.copy()))

print(oxy * co2)