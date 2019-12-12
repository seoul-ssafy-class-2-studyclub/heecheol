from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def push_left(board2):
    board = [row[:] for row in board2]
    for row in range(N):
        i = k = 0
        while i < N:
            if board[row][i] == 0:
                i += 1
                continue
            temp, board[row][i] = board[row][i], 0
            j = i + 1
            i += 1
            while j < N:
                if board[row][j] == 0:
                    j += 1
                    continue
                if board[row][j] == temp:
                    temp *= 2
                    board[row][j] = 0
                    i = j + 1
                    break
                else:
                    i = j
                    break
            board[row][k] = temp
            k += 1
    return board


def push_right(board2):
    board = [row[:] for row in board2]
    for row in range(N):
        i = k = N - 1
        while i >= 0:
            if board[row][i] == 0:
                i -= 1
                continue
            temp, board[row][i] = board[row][i], 0
            j = i - 1
            i -= 1
            while j >= 0:
                if board[row][j] == 0:
                    j -= 1
                    continue
                if board[row][j] == temp:
                    temp *= 2
                    board[row][j] = 0
                    i = j - 1
                    break
                else:
                    i = j
                    break
            board[row][k] = temp
            k -= 1
    return board


def push_down(board2):
    board = [row[:] for row in board2]
    for col in range(N):
        i = k = N - 1
        while i >= 0:
            if board[i][col] == 0:
                i -= 1
                continue
            temp, board[i][col] = board[i][col], 0
            j = i - 1
            i -= 1
            while j >= 0:
                if board[j][col] == 0:
                    j -= 1
                    continue
                if board[j][col] == temp:
                    temp *= 2
                    board[j][col] = 0
                    i = j - 1
                    break
                else:
                    i = j
                    break

            board[k][col] = temp
            k -= 1

    return board


def push_up(board2):
    board = [row[:] for row in board2]
    for col in range(N):
        i = k = 0
        while i < N:
            if board[i][col] == 0:
                i += 1
                continue
            temp, board[i][col] = board[i][col], 0
            j = i + 1
            i += 1
            while j < N:
                if board[j][col] == 0:
                    j += 1
                    continue
                if board[j][col] == temp:
                    temp *= 2
                    board[j][col] = 0
                    i = j + 1
                    break
                else:
                    i = j
                    break
            board[k][col] = temp
            k += 1

    return board


def solution(board1, n, m):
    global max_num
    if n == 5:
        t = max([max(row) for row in board1])
        if max_num < t:
            max_num = t
        return
    else:
        for i in range(4):
            if i == m:
                continue
            if i == 0:
                board3 = push_left(board1)
            elif i == 1:
                board3 = push_up(board1)
            elif i == 2:
                board3 = push_right(board1)
            else:
                board3 = push_down(board1)
            solution(board3, n + 1, i)


N = int(input())
board0 = [list(map(int, input().split())) for _ in range(N)]
max_num = 0

for i in range(4):
    solution(board0, 0, i)

print(max_num)

