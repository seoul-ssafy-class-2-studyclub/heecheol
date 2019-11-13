import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * (M + K) for _ in range(N + K)]
    status = [[[] for _ in range(M + K)] for _ in range(N + K)]    # 0 : 빈 공간, 1 : 비활성상태, 2 : 활성상태, 3 : 죽은 상태, 4: 생성 예정

    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(N):
        for j in range(M):
            if data[i][j] != 0:
                board[i + K // 2][j + K // 2] = data[i][j]
                status[i + K // 2][j + K // 2] = [1, data[i][j]]

    for k in range(K):
        for i in range(N + K):
            for j in range(M + K):
                if status[i][j]:
                    if status[i][j][0] == 1:    # 비활성상태
                        if status[i][j][1] == 1:
                            status[i][j][0] = 2
                            status[i][j][1] = board[i][j]
                        else:
                            status[i][j][1] -= 1

                    elif status[i][j][0] == 2:
                        for adj in adj_list:
                            nxt1, nxt2 = i + adj[0], j + adj[1]
                            if not status[nxt1][nxt2]:
                                status[nxt1][nxt2] = [4, 0]
                        if status[i][j][1] == 1:
                            status[i][j][0] = 3
                        else:
                            status[i][j][1] -= 1

        for i in range(N + K):
            for j in range(M + K):
                if status[i][j]:
                    if status[i][j][0] == 4:
                        value = []
                        for adj in adj_list:
                            nxt1 = i + adj[0]
                            nxt2 = j + adj[1]
                            if 0 <= nxt1 < N + K and 0 <= nxt2 < M + K:
                                if status[nxt1][nxt2]:
                                    if status[nxt1][nxt2][0] == 2:
                                        if status[nxt1][nxt2][1] != board[nxt1][nxt2]:
                                            value.append(board[nxt1][nxt2])

                                    elif status[nxt1][nxt2] == [3, 1]:
                                        value.append(board[nxt1][nxt2])
                        status[i][j][0] = 1
                        status[i][j][1] = max(value)
                        board[i][j] = max(value)

    cnt = 0
    for i in range(N + K):
        for j in range(M + K):
            if status[i][j]:
                if 0 < status[i][j][0] < 3:
                    cnt += 1

    print('#{} {}'.format(tc, cnt))
