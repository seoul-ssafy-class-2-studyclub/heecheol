import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[True] * N for _ in range(N)]

flag = True
for k in range(N):
    for i in range(N):
        if i != k:
            for j in range(N):
                if j != k and i != j:
                    if board[i][j] > board[i][k] + board[k][j]:
                        flag = False
                        break
                    elif board[i][j] == board[i][k] + board[k][j] and visit[i][j] is True:
                        visit[i][j] = False
            if flag is False:
                break
    if flag is False:
        break
if flag is False:
    print(-1)
else:
    result = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            if visit[i][j] is True:
                result += board[i][j]
    print(result)

