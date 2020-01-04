import sys
sys.stdin = open('input.txt', 'r')


n = int(input())
nums = list(map(int, input().split()))
result = max(nums)

for i in range(n):
    if nums[i] <= 0:
        continue
    temp = nums[i]
    for j in range(i + 1, n):
        temp += nums[j]
        if temp > result:
            result = temp

print(result)
