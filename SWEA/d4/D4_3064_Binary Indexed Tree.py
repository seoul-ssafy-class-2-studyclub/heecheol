import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    nums = [0]
    nums.extend(list(map(int, input().split())))

    result = []
    for i in range(M):
        C, A, B = map(int, input().split())
        if C == 1:
            nums[A] += B
        else:
            result.append(str(sum(nums[A:B+1])))

    result = ' '.join(result)
    print('#{} {}'.format(tc, result))
