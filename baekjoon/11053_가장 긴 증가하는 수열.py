import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N
max_length = 0

for i in range(N):
    temp = 0
    for j in range(i - 1, -1, -1):
        if nums[j] < nums[i] and temp < dp[j]:
            temp = dp[j]
    dp[i] = temp + 1
    if dp[i] > max_length:
        max_length = dp[i]

print(max_length)
