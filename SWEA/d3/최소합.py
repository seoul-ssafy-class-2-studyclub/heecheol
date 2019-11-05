def path(i=0, j=0):
    global route
    global min_value
    if i == N - 1 and j == N - 1:
        if route < min_value:
            min_value = route

    else:
        for ne in nxt:
            idx1 = i + ne[0]
            idx2 = j + ne[1]
            if 0 <= idx1 < N and 0 <= idx2 < N:
                route += board[idx1][idx2]
                if route < min_value:
                    path(idx1, idx2)
                route -= board[idx1][idx2]


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]

    nxt = [[0, 1], [1, 0]]
    route = board[0][0]
    ways = []
    min_value = 9999999
    path()
    print('#{} {}'.format(tc, min_value))