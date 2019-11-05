import sys
sys.stdin = open('input_1.txt', 'r')


def route(cnt, flag):


    if stack:
        print(stack)
        idx1, idx2 = stack.pop()
        if visited[idx1][idx2] == False:
            visited[idx1][idx2] = True


            for adj in adj_list:
                nxt1 = idx1 + adj[0]
                nxt2 = idx2 + adj[1]

                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if board[nxt1][nxt2] <= board[idx1][idx2] and visited[nxt1][nxt2] == False:
                        stack.append((nxt1, nxt2))
                        route(cnt+1, flag)

                    elif flag == True:
                        if board[nxt1][nxt2] - K <= board[idx1][idx2]:
                            flag = False
                            temp2 = board[nxt1][nxt2]
                            board[nxt1][nxt2] = board[idx1][idx2]
                            stack.append((nxt1, nxt2))
                            route(cnt+1, flag)
                            board[nxt1][nxt2] = temp2
                            flag = True


            visited[idx1][idx2] = False


TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N for _ in range(N)]

    idx_list = []
    highest = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > highest:
                idx_list = [(i, j)]
                highest = board[i][j]
            elif board[i][j] == highest:
                idx_list.append((i, j))

    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for idx in idx_list:
        flag = True
        stack = [idx]
        cnt = 1
        max_cnt = 0
        route(cnt, flag)


