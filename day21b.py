import fileinput
from typing import Dict, Tuple
from collections import defaultdict

input = map(str.rstrip, fileinput.input())

first_line = next(input)
_, p1_pos_str = first_line.split(": ")
p1_pos = int(p1_pos_str)

second_line = next(input)
_, p2_pos_str = second_line.split(": ")
p2_pos = int(p2_pos_str)

MultiplicityMap = Dict[Tuple[int, int], int]

p1_won = 0
p2_won = 0

p1_states = defaultdict(int)
p2_states = defaultdict(int)

p1_states[(p1_pos, 0)] = 1
p2_states[(p2_pos, 0)] = 1

rolls = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def roll(states: MultiplicityMap) -> MultiplicityMap:
    new_states = defaultdict(int)
    for (position, score), multiplicity in states.items():
        for advance, count in rolls:
            new_position = ((position - 1) + advance) % 10 + 1
            new_states[(new_position, score + new_position)] += multiplicity * count

    return new_states


while p1_states and p2_states:
    p1_new_states = defaultdict(int)
    for (p1_position, p1_score), p1_multiplicity in p1_states.items():
        for p1_advance, p1_count in rolls:
            p1_new_position = ((p1_position - 1) + p1_advance) % 10 + 1
            p1_new_score = p1_score + p1_new_position
            p1_new_multiplicity = p1_multiplicity * p1_count
            if p1_new_score >= 21:
                p1_won += p1_new_multiplicity * sum(p2_states.values())
            else:
                p1_new_states[(p1_new_position, p1_new_score)] += p1_new_multiplicity

    p2_new_states = defaultdict(int)
    for (p2_position, p2_score), p2_multiplicity in p2_states.items():
        for p2_advance, p2_count in rolls:
            p2_new_position = ((p2_position - 1) + p2_advance) % 10 + 1
            p2_new_score = p2_score + p2_new_position
            p2_new_multiplicity = p2_multiplicity * p2_count
            if p2_new_score >= 21:
                p2_won += p2_new_multiplicity * sum(p1_new_states.values())
            else:
                p2_new_states[(p2_new_position, p2_new_score)] += p2_new_multiplicity

    p1_states = p1_new_states
    p2_states = p2_new_states


print(max(p1_won, p2_won))
