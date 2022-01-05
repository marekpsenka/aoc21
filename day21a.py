import fileinput

input = map(str.rstrip, fileinput.input())

first_line = next(input)
_, p1_pos_str = first_line.split(": ")
p1_pos = int(p1_pos_str)

second_line = next(input)
_, p2_pos_str = second_line.split(": ")
p2_pos = int(p2_pos_str)

die = 0
roll_count = 0
p1_score = 0
p2_score = 0


def roll():
    global die
    global roll_count
    if die == 100:
        die = 1
    else:
        die += 1
    roll_count += 1
    return die


while True:
    p1_pos = ((p1_pos - 1) + sum([roll() for _ in range(3)])) % 10 + 1
    p1_score += p1_pos
    if p1_score >= 1000:
        print(p2_score * roll_count)
        break
    p2_pos = ((p2_pos - 1) + sum([roll() for _ in range(3)])) % 10 + 1
    p2_score += p2_pos
    if p2_score >= 1000:
        print(p1_score * roll_count)
        break