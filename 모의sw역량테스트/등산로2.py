import sys
sys.stdin = open('input_1.txt', 'r')

def route(idx1, idx2, cnt, flag):
    global max_cnt
    if max_cnt < cnt:
        max_cnt = cnt
    visited[idx1][idx2] = True
    print(idx1, idx2, cnt)
    for adj in adj_list:
        nxt1 = idx1 + adj[0]
        nxt2 = idx2 + adj[1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if board[nxt1][nxt2] < board[idx1][idx2] and visited[nxt1][nxt2] is False:
                route(nxt1, nxt2, cnt + 1, flag)
                visited[nxt1][nxt2] = False
            elif flag is True and board[nxt1][nxt2] - K < board[idx1][idx2] and visited[nxt1][nxt2] is False:
                visited[nxt1][nxt2] = True
                print(nxt1, nxt2, cnt+1)
                print('-- flag --')
                if max_cnt < cnt+1:
                    max_cnt = cnt+1
                for adj2 in adj_list:
                    nxt3 = nxt1 + adj2[0]
                    nxt4 = nxt2 + adj2[1]
                    if 0 <= nxt3 < N and 0 <= nxt4 < N:
                        if board[nxt3][nxt4] < board[idx1][idx2] - 1 and visited[nxt3][nxt4] is False:
                            route(nxt3, nxt4, cnt+2, False)
                            print('q')
                            visited[nxt3][nxt4] = False
                    visited[nxt1][nxt2] = False



TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    s_list = []
    highest = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > highest:
                s_list = [(i, j)]
                highest = board[i][j]
            elif board[i][j] == highest:
                s_list.append((i, j))
    max_cnt = 0
    for idx in s_list:
        visited = [[False] * N for _ in range(N)]
        route(idx[0], idx[1], 1, True)
    print('#{} {}'.format(tc, max_cnt))
