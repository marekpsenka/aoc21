import fileinput
from collections import defaultdict

input = map(str.rstrip, fileinput.input())

template = next(input)
next(input)  # discard blank line

rules = dict()

for line in input:
    pair, ins = line.split(" -> ")
    rules[(pair[0], pair[1])] = ins


def apply_process(t):
    nt = []
    for i in range(len(t) - 1):
        nt.append(t[i])
        maybe_ins = rules.get((t[i], t[i + 1]))
        if maybe_ins is not None:
            nt.append(maybe_ins)

    nt.append(t[-1])

    return nt


occurences = defaultdict(int)

for i in range(10):
    template = apply_process(template)

for c in template:
    occurences[c] += 1

most_frequent = max(occurences, key=occurences.get)
least_frequent = min(occurences, key=occurences.get)

print(occurences[most_frequent] - occurences[least_frequent])
