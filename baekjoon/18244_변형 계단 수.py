from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
nums = [[0] * 13 for _ in range(N + 3)]
nums[0] = [1] * 10 + [0] * 3

for i in range(1, N):
    for j in range(10):
        nums[i][j] = nums[i-1][j-1] + nums[i-1][j+1] - nums[i-3][j-3] - nums[i-3][j+3]

pprint(nums)
print(sum(nums[N - 1]) % 1000000007)
