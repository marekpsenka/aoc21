
import fileinput
import itertools

input = map(str.rstrip, fileinput.input())

numbers = [int(s) for s in next(input).split(",")]

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

def unmarked_sum(board, drawn):
    return sum([i for i in itertools.chain(*board) if i not in drawn])

drawnCount = 5
survivingBoards = []

while True:
    for board in boards:
        if not board_has_bingo(board, numbers[:drawnCount]):
            survivingBoards.append(board)

    drawnCount += 1
    boards = survivingBoards
    survivingBoards = []

    if len(boards) == 1:
        break

while not board_has_bingo(boards[0], numbers[:drawnCount]):
    drawnCount += 1

usum = unmarked_sum(boards[0], numbers[:drawnCount])
num = numbers[drawnCount - 1]

print(usum * num)

