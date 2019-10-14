from time import time
import sys
sys.stdin = open('input.txt', 'r')


def put(left, right, idx):
    global cnt

    if idx == N:
        cnt += 1

    else:
        for i in range(N):
            if visit[i] is False:
                visit[i] = True
                if left >= right + weights[i]:
                    put(left, right + weights[i], idx + 1)
                put(left + weights[i], right, idx + 1)
                visit[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    visit = [False] * N
    cnt = 0
    put(0, 0, 0)
    print('#{} {}'.format(tc, cnt))