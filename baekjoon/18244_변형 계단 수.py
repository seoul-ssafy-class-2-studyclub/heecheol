from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
if N == 1:
    print(10)

else:
    board = [[[0, 0, 0, 0] for _ in range(11)] for _ in range(N)]
    board[1] = [[1, 0, 1, 0] for _ in range(11)]
    board[1][0][0] = 0
    board[1][9][2] = 0
    board[1][10] = [0, 0, 0, 0]

    for i in range(2, N):
        for j in range(10):
            board[i][j][0] = board[i - 1][j - 1][2] + board[i - 1][j - 1][3]
            board[i][j][1] = board[i - 1][j - 1][0]
            board[i][j][2] = board[i - 1][j + 1][0] + board[i - 1][j + 1][1]
            board[i][j][3] = board[i - 1][j + 1][2]

    result = sum(sum(row) for row in board[N - 1])
    print(result % 1000000007)
