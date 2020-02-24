import sys
sys.stdin = open('input.txt', 'r')


def func18430(idx1, idx2, vis, temp):
    global result

    if idx1 == N - 1 and idx2 == M - 1:
        flag = True
        sum_near = 0
        for adj in adj_end_point:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M and vis[nxt1][nxt2] is False:
                sum_near += board[nxt1][nxt2]
            else:
                flag = False
                break

        if flag is True:
            temp += sum_near + board[idx1][idx2] * 2

        if temp > result:
            result = temp
        return

    if vis[idx1][idx2] is False:
        for adj_list in adj_lists:
            flag = True
            sum_near = 0
            nxt_vis = [row[:] for row in vis]

            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M and vis[nxt1][nxt2] is False:
                    nxt_vis[nxt1][nxt2] = True
                    sum_near += board[nxt1][nxt2]
                else:
                    flag = False
                    break

            if flag is False:
                continue

            else:
                nxt_vis[idx1][idx2] = True
                sum_near += board[idx1][idx2] * 2

                if idx2 == M - 1:
                    func18430(idx1 + 1, 0, nxt_vis, temp + sum_near)
                else:
                    func18430(idx1, idx2 + 1, nxt_vis, temp + sum_near)

    if idx2 == M - 1:
        func18430(idx1 + 1, 0, vis, temp)
    else:
        func18430(idx1, idx2 + 1, vis, temp)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_lists = [[(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)], [(-1, 0), (0, 1)]]
adj_end_point = [(-1, 0), (0, -1)]
visit = [[False] * M for _ in range(N)]

result = 0
func18430(0, 0, visit, 0)

print(result)
