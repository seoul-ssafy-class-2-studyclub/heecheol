import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = rgb[0]

for i in range(1, N):
    for j in range(3):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb[i][2]

print(min(dp[-1]))
