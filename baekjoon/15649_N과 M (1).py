import sys
sys.stdin = open('input.txt', 'r')


def solution(k, arr):
    if k == M:
        print(' '.join(arr))
        return
    else:
        for num in nums:
            if num not in arr:
                solution(k + 1, arr + [num])


N, M = map(int, input().split())
nums = list(map(str, range(1, N + 1)))
solution(0, [])
