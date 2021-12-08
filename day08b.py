#   0: 6    1: 2    2: 5    3: 5    4: 4                                       
#  aaaa    ....    aaaa    aaaa    ....     2| 1                               
# b    c  .    c  .    c  .    c  b    c    3| 7                               
# b    c  .    c  .    c  .    c  b    c    4| 4                               
#  ....    ....    dddd    dddd    dddd     5| 5,2,3                           
# e    f  .    f  e    .  .    f  .    f    6| 6,9,0                           
# e    f  .    f  e    .  .    f  .    f    7| 8                               
#  gggg    ....    gggg    gggg    ....                                        
#                                                                              
#   5: 5    6: 6    7: 3    8: 7    9: 6    0| a b c   e f g                   
#  aaaa    aaaa    aaaa    aaaa    aaaa     1|     c     f                     
# b    .  b    .  .    c  b    c  b    c    2| a   c d e   g                   
# b    .  b    .  .    c  b    c  b    c    3| a   c d   f g                   
#  dddd    dddd    ....    dddd    dddd     4|   b c d   f                     
# .    f  e    f  .    f  e    f  .    f    5| a b   d   f g                   
# .    f  e    f  .    f  e    f  .    f    6| a b   d e f g                   
#  gggg    gggg    ....    gggg    gggg     7| a   c     f                     
#                                           8| a b c d e f g                   
#                                           9| a b c d   f g                   
#                                             --------------                   
#                                              8 6 8 7 4 9 7                   

import fileinput
from collections import defaultdict

input = map(str.rstrip, fileinput.input())

total = 0

for line in input:
    frequency = defaultdict(int)
    segment_map = dict()
    inverse_map = dict()
    patterns_str, digits_str = str.split(line, " | ")
    for p in patterns_str.split(" "):
        if len(p) == 2:
            two_segment_pattern = p
        if len(p) == 3:
            three_segment_pattern = p
        if len(p) == 4:
            four_segment_pattern = p
        for c in p:
            frequency[c] += 1

    for k, v in frequency.items():
        if v == 4:
            segment_map[k] = "e"
        if v == 9:
            segment_map[k] = "f"
            inverse_of_f = k
        if v == 6:
            segment_map[k] = "b"

    if two_segment_pattern[0] == inverse_of_f:
        segment_map[two_segment_pattern[1]] = "c"
    elif two_segment_pattern[1] == inverse_of_f:
        segment_map[two_segment_pattern[0]] = "c"

    maps_to_a = list(set(three_segment_pattern) - set(two_segment_pattern))[0]
    segment_map[maps_to_a] = "a"

    maps_to_d = [c for c in four_segment_pattern if c not in segment_map.keys()][0]
    segment_map[maps_to_d] = "d"

    maps_to_g = list(set("abcdefg") - segment_map.keys())[0]
    segment_map[maps_to_g] = "g"

    def transform(s):
        return set([segment_map[c] for c in s])

    def get_digit(s):
        if len(s) == 2:
            return 1
        if len(s) == 3:
            return 7
        if len(s) == 4:
            return 4
        if len(s) == 7:
            return 8

        t = transform(s)
        if t == set("abcefg"):
            return 0
        if t == set("acdeg"):
            return 2
        if t == set("acdfg"):
            return 3
        if t == set("abdfg"):
            return 5
        if t == set("abdefg"):
            return 6
        if t == set("abcdfg"):
            return 9
    fst, snd, thr, frt = digits_str.split(" ")
    total += get_digit(fst) * 1000 + get_digit(snd) * 100 + get_digit(thr) * 10 + get_digit(frt)

print(total)



