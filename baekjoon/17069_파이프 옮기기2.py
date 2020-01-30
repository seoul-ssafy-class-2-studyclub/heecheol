# from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
board[1][0] = 1

dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(N):
        if board[i][j]:
            continue

        if j > 0 and board[i][j - 1] == 0:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            if i > 0 and board[i - 1][j] == 0:
                dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
                if board[i - 1][j - 1] == 0:
                    dp[i][j][1] = sum(dp[i - 1][j - 1])
        elif i > 0 and board[i - 1][j] == 0:
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]

# pprint(dp)
print(sum(dp[N-1][N-1]))
