import sys
sys.stdin = open('input.txt', 'r')


def solution(n, k, arr):
    if k == M:
        print(' '.join(arr))
        return
    else:
        for i in range(n, N):
            solution(i + 1, k + 1, arr + [nums[i]])


N, M = map(int, input().split())
nums = list(map(str, range(1, N + 1)))
solution(0, 0, [])
