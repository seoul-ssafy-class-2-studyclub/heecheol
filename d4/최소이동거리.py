import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())

    inf = 987654321
    arr = [0] + [inf for _ in range(N)]

    visit = [False] * (N + 1)
    adj_list = [[inf] * (N + 1) for _ in range(N + 1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1][n2] = w

    nxt = 0
    while True:
        min_value = inf

        for i in range(1, N + 1):
            if visit[i] is False and min_value > arr[i]:
                min_value = arr[i]
                nxt = i
        if nxt == N:
            break
        else:
            visit[nxt] = True
            for i in range(1, N + 1):
                if visit[i] is False:
                    arr[i] = min(arr[i], arr[nxt] + adj_list[nxt][i])

    print('#{} {}'.format(tc, min_value))
    