import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
result = []
for tc in range(T):
    N = int(input())
    nums = ['_'] * N
    for i in range(N):
        nums[i] = input()

    nums.sort()

    flag = True
    for i in range(N - 1):
        if len(nums[i]) >= len(nums[i + 1]):
            continue
        if nums[i] == nums[i + 1][:len(nums[i])]:
            flag = False
            break

    if flag is False:
        result.append('NO')
    else:
        result.append('YES')

print('\n'.join(result))
