import fileinput

horizontal = 0
vertical = 0

for line in fileinput.input():
    dir, amt = line.split()
    if dir == "forward":
        horizontal += int(amt)
    elif dir == "up":
        vertical -= int(amt)
    elif dir == "down":
        vertical += int(amt)

print (horizontal * vertical)