import fileinput


def closes(brace1, brace2):
    if brace1 == ")":
        return brace2 == "("
    if brace1 == "]":
        return brace2 == "["
    if brace1 == "}":
        return brace2 == "{"
    if brace1 == ">":
        return brace2 == "<"


def get_score(brace):
    if brace == "(":
        return 1
    if brace == "[":
        return 2
    if brace == "{":
        return 3
    if brace == "<":
        return 4


input = map(str.rstrip, fileinput.input())

scores = []

for line in input:
    it = iter(line)
    stack = [next(it)]
    corrupted = False
    for c in it:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        elif closes(c, stack[-1]):
            stack.pop()
        else:
            corrupted = True
            break

    if corrupted:
        continue

    this_score = 0
    for c in reversed(stack):
        this_score *= 5
        this_score += get_score(c)

    scores.append(this_score)

scores.sort()
print(scores[(len(scores) - 1) // 2])
