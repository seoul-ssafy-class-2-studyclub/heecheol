import sys
sys.stdin = open('input.txt', 'r')


def solution(k, c, n):
    global cnt

    if k == N - 1:
        cnt += 1
        return

    if c > 0:
        if c == 2:
            solution(k + 1, -1, n - 1)
            return
        if n + 1 <= 9:
            solution(k + 1, c + 1, n + 1)
            solution(k + 1, -1, n - 1)
        else:
            solution(k + 1, -1, n - 1)
        return

    elif c < 0:
        if c == -2:
            solution(k + 1, 1, n + 1)
            return
        if n - 1 >= 0:
            solution(k + 1, 1, n + 1)
            solution(k + 1, c - 1, n - 1)
        else:
            solution(k + 1, 1, n + 1)
        return

    else:
        if 0 < n < 9:
            solution(k + 1, 1, n + 1)
            solution(k + 1, -1, n - 1)
        elif n == 0:
            solution(k + 1, 1, n + 1)
        else:
            solution(k + 1, -1, n - 1)
        return


N = int(input())
cnt = 0
for i in range(10):
    solution(0, 0, i)
print(cnt % 1000000007)
