import fileinput

horizontal = 0
vertical = 0
aim = 0

for line in fileinput.input():
    dir, amt = line.split()
    if dir == "forward":
        horizontal += int(amt)
        vertical += aim * int(amt)
    elif dir == "up":
        aim -= int(amt)
    elif dir == "down":
        aim += int(amt)

print (horizontal * vertical)