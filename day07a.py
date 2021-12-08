import fileinput

input = map(str.rstrip, fileinput.input())

pos = [int(s) for s in next(input).split(",")]

min_fuel = sum(pos)
fuel = 0
for i in range(min(pos), max(pos)):
    for p in pos:
        fuel += abs(p - i)

    if fuel < min_fuel:
        min_fuel = fuel
        
    fuel = 0

print(min_fuel)