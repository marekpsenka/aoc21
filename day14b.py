import fileinput
from collections import defaultdict

input = map(str.rstrip, fileinput.input())

template = next(input)
next(input)  # discard blank line

rules = dict()

for line in input:
    pair, ins = line.split(" -> ")
    rules[pair] = ins


pairs = defaultdict(int)
occurences = defaultdict(int)

for c in template:
    occurences[c] += 1

for c1, c2 in zip(template, template[1:]):
    pairs[c1 + c2] += 1

for _ in range(40):
    for (c1, c2), count in pairs.copy().items():
        c = rules[c1 + c2]
        pairs[c1 + c2] -= count
        pairs[c1 + c] += count
        pairs[c + c2] += count
        occurences[c] += count


most_frequent = max(occurences, key=occurences.get)
least_frequent = min(occurences, key=occurences.get)

print(occurences[most_frequent] - occurences[least_frequent])
