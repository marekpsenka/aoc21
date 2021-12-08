import fileinput
import sys

input = map(str.rstrip, fileinput.input())

pos = [int(s) for s in next(input).split(",")]

min_fuel = sys.maxsize
fuel = 0
for i in range(min(pos), max(pos)):
    for p in pos:
        for j in range(1, abs(p - i) + 1):
            fuel += j

    if fuel < min_fuel:
        min_fuel = fuel
        
    fuel = 0

print(min_fuel)


