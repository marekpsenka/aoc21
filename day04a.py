import fileinput
import itertools

input = map(str.rstrip, fileinput.input())

numbers = [int(s) for s in next(input).split(",")]

print(numbers)

boards = []

while(True):
    try:
        next(input)
        lines = map(str.split, itertools.islice(input, 5))
        linesOfInts = [[int(s) for s in l] for l in lines]
        boards.append(linesOfInts)
    except StopIteration:
        break

def column_has_bingo(board, drawn, i):
    return all([board[j][i] in drawn for j in range(len(board))])

def row_has_bingo(board, drawn, i):
    return all(x in drawn for x in board[i])

def board_has_bingo(board, drawn):
    for i in range(len(board)):
        if row_has_bingo(board, drawn, i) or column_has_bingo(board, drawn, i):
            return True

    return False

found = False
drawnCount = 5
result = 0

while not found:
    for board in boards:
        if board_has_bingo(board, numbers[:drawnCount]):
            found = True
            unmarkedSum = sum([i for i in itertools.chain(*board) if i not in numbers[:drawnCount]])
            result = unmarkedSum * numbers[drawnCount - 1]
            break

    drawnCount += 1

print(result)

