import sys
sys.stdin = open('input_1.txt', 'r')


def route():
    while stack:
        idx1, idx2, cnt, flag = stack.pop()
        if visited[idx1][idx2] == False:
            visited[idx1][idx2] = True


            for adj in adj_list:
                nxt1 = idx1 + adj[0]
                nxt2 = idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if board[nxt1][nxt2] <= board[idx1][idx2] and visited[nxt1][nxt2] is False:
                        stack.append([nxt1, nxt2, cnt+1, flag])

                    elif flag is True and board[nxt1][nxt2] - K <= board[idx1][idx2]:
                        visited[nxt1][nxt2] = True

                        for adj2 in adj_list:
                            nxt3 = nxt1 + adj2[0]
                            nxt4 = nxt2 + adj2[1]
                            if 0 <= nxt3 < N and 0 <= nxt4 < N:
                                if board[nxt3][nxt4] <= board[idx1][idx2] and visited[nxt3][nxt4] is False:
                                    stack.append([nxt3, nxt4, cnt+2, False])
            else:
                visited[idx1][idx2] = False



TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    s_list = []
    highest = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > highest:
                s_list = [(i, j)]
                highest = board[i][j]
            elif board[i][j] == highest:
                s_list.append((i, j))

    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for idx in s_list:
        stack = [[idx[0], idx[1], 1, True]]

        route()


