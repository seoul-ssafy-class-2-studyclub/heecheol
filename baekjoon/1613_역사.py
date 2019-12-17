import sys
sys.stdin = open('input.txt', 'r')


n, k = map(int, input().split())
board = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(k):
    i, j = map(int, input().split())
    board[i][j] = -1
    board[j][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        if i != k and board[i][k] != 0:
            for j in range(i + 1, n + 1):
                if j != k and board[i][j] == 0 and board[i][k] == board[k][j]:
                    board[i][j] = board[i][k]
                    board[j][i] = - board[i][k]


N = int(input())
result = [0] * N
for k in range(N):
    i, j = map(int, input().split())
    result[k] = str(board[i][j])

print('\n'.join(result))
