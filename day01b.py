import fileinput
import itertools

def by_triples(iterable):
    a, b, c = itertools.tee(iterable, 3)
    next(b)
    next(c)
    next(c)
    return zip(a, b, c)

acc = 0
triples = by_triples(map(int, fileinput.input()))
x, y, z = next(triples)
last_sum = x + y + z

for x, y, z in triples:
    s = x + y + z
    if s > last_sum:
        acc += 1

    last_sum = s

print(acc)