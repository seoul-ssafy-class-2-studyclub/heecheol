from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):

    flat = 1
    for j in range(1, N):
        if board[i][j] == board[i][j-1]:
            flat += 1
        elif board[i][j] == board[i][j-1] + 1:
            if flat >= L:
                flat = 1
            else:
                break
        elif board[i][j] == board[i][j-1] - 1:
            if flat < 0:
                break
            else:
                flat = -L + 1
        else:
            break
    else:
        if flat < 0:
            continue
        cnt += 1

for j in range(N):

    flat = 1
    for i in range(1, N):
        if board[i][j] == board[i-1][j]:
            flat += 1
        elif board[i][j] == board[i-1][j] + 1:
            if flat >= L:
                flat = 1
            else:
                break
        elif board[i][j] == board[i-1][j] - 1:
            if flat < 0:
                break
            else:
                flat = -L + 1
        else:
            break
    else:
        if flat < 0:
            continue
        cnt += 1

print(cnt)
