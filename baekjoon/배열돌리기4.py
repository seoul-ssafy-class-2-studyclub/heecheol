from pprint import pprint
import itertools
import sys
sys.stdin = open('input.txt', 'r')

N, M, K = map(int, input().split())

board3 = [list(map(int, input().split())) for _ in range(N)]

arr = []
for _ in range(K):
    arr.append(list(map(int, input().split())))

orders = list(itertools.permutations(list(range(K))))
min_value = 987654321

# pprint(board3)

for order in orders:
    board = [row[:] for row in board3]
    # print(order)
    for idx in order:
        r, c, s = arr[idx]
        board2 = [row[:] for row in board]
        r, c = r - 1, c - 1
        for t in range(1, s + 1):
            # 위
            for i in range(c-t, c+t):
                board[r-t][i+1] = board2[r-t][i]
            for i in range(r-t, r+t):
                board[i+1][c+t] = board2[i][c+t]
            for i in range(c-t+1, c+t+1):
                board[r+t][i-1] = board2[r+t][i]
            for i in range(r-t+1, r+t+1):
                board[i-1][c-t] = board2[i][c-t]

        # pprint(board)

    for row in board:
        sum_row = sum(row)
        if sum_row < min_value:
            min_value = sum_row

print(min_value)