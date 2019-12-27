from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == '.' or board[i][j] == '#':
            continue
        if board[i][j] == 'S':
            si, sj = i, j

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 위 0, 오 1, 아 2, 왼 3
nd = [[1, 3], [0, 2], [1, 3], [0, 2], [0, 1, 2, 3]]
visit = [[False] * M for _ in range(N)]

queue = [(si, sj, 4, 0, 0, visit)]

flag = True
while queue:
    idx1, idx2, k, m, cnt, visited = queue.pop(0)
    vis = [row[:] for row in visited]
    vis[idx1][idx2] = True
    pprint(vis)
    for i in nd[k]:
        nxt1, nxt2 = idx1 + adj_list[i][0], idx2 + adj_list[i][1]
        if 0 <= nxt1 < N and 0 <= nxt2 < M:
            if vis[nxt1][nxt2] is False:
                if board[nxt1][nxt2] == 'C':
                    if cnt == 1:
                        flag = False
                        break
                    queue.append((nxt1, nxt2, i, m + 1, cnt + 1, vis))
                    continue
                if board[nxt1][nxt2] == '.':
                    queue.append((nxt1, nxt2, i, m + 1, cnt, vis))
                    continue
    if flag is False:
        break
if flag is False:
    print(m + 1)
else:
    print(-1)
