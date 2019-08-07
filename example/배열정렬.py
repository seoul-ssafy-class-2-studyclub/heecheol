from pprint import pprint

board = [[9, 20, 2, 18, 11],
        [19, 1, 25, 3, 21],
        [8, 24, 10, 17, 7],
        [15, 4, 16, 5, 6],
        [12, 13, 22, 23, 14]]

def min_index(num):
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                return i, j

point = [5, 9, 13, 16, 19, 21, 23, 24]

i = j = 0
num = 1

flag = 0
while num <= 25:
    index = min_index(num)
    board[i][j], board[index[0]][index[1]] = board[index[0]][index[1]], board[i][j]
    if num in point:
        flag += 1
    if flag % 4 == 0:
        j += 1
    elif flag % 4 == 1:
        i += 1
    elif flag % 4 == 2:
        j -= 1
    else:
        i -= 1
    num += 1
    pprint(board)

# pprint(board)

