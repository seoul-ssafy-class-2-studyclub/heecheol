import sys
sys.stdin = open('input.txt', 'r')


def sorting(left, right, n):
    if left == right:
        nums.insert(left, n)
        return

    m = (left + right) // 2
    if n > nums[m]:
        sorting(m + 1, right, n)

    elif n == nums[m]:
        nums.insert(m, n)

    else:
        sorting(left, m, n)

    return


N = int(input())
nums = []
result = []
for _ in range(N):
    num = int(input())
    length = len(nums)
    sorting(0, len(nums), num)
    result.append(str(nums[length // 2]))

print('\n'.join(result))

