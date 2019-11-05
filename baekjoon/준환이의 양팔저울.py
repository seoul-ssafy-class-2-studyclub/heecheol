import sys
sys.stdin = open('input.txt', 'r')


def put(left, right, idx):
    global cnt

    if idx == N:
        cnt += 1

    else:
        for ii in range(N):
            if visit[ii] is False:
                visit[ii] = True
                if left >= right + weights[ii]:
                    put(left, right + weights[ii], idx + 1)
                put(left + weights[ii], right, idx + 1)
                visit[ii] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    weights = list(map(int, input().split()))
    visit = [False] * N
    cnt = 0
    for i in range(N):
        visit[i] = True
        put(weights[i], 0, 1)
        visit[i] = False
    print('#{} {}'.format(tc, cnt))