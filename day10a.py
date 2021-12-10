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
    if brace == ")":
        return 3
    if brace == "]":
        return 57
    if brace == "}":
        return 1197
    if brace == ">":
        return 25137


input = map(str.rstrip, fileinput.input())

score = 0

for line in input:
    it = iter(line)
    stack = [next(it)]
    for c in it:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        elif closes(c, stack[-1]):
            stack.pop()
        else:
            score += get_score(c)
            break

print(score)
