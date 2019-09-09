import sys
sys.stdin = open('input.txt', 'r')


def bingo(board):
    cnt = 0
    r_cross = []
    l_cross = []
    for row in range(5):
        if board[row] == [-1, -1, -1, -1, -1]:
            cnt += 1
        l_cross.append(board[row][row])
        r_cross.append(board[row][4-row])

    if l_cross == [-1, -1, -1, -1, -1]:
        cnt += 1
    if r_cross == [-1, -1, -1, -1, -1]:
        cnt += 1

    for col in range(5):
        for row in range(5):
            if board[row][col] != -1:
                break
        else:
            cnt += 1
    if cnt >= 3:
        return True
    else:
        return False


board = [input().split() for i in range(5)]

speak = []
for i in range(5):
    speak += input().split()

for i in range(25):
    num = speak[i]
    for row in range(5):
        if num in board[row]:
            k = board[row].index(num)
            board[row][k] = -1
            break
    if i >= 11:
        if bingo(board) == True:
            print(i+1)
            break
