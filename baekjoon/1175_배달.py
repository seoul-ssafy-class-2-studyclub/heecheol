import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

si = sj = 0
cc = 1

for i in range(N):
    for j in range(M):
        if board[i][j] == '.' or board[i][j] == '#':
            continue
        if board[i][j] == 'C':
            board[i][j] = cc
            cc += 1
        else:
            si, sj = i, j
            board[si][sj] = '.'

adj_list = [[(N, M), (1, 0), (0, -1), (-1, 0)], [(0, 1), (N, M), (0, -1), (-1, 0)], [(0, 1), (1, 0), (N, M), (-1, 0)], [(0, 1), (1, 0), (0, -1), (N, M)], [(0, 1), (1, 0), (0, -1), (-1, 0)]]
# print(board)
visit = [[[[False, False, False, False] for i in range(3)] for j in range(M)] for k in range(N)]
# print(visit)

queue = [(si, sj, 0, 4, 0)]    # idx1, idx2, num_visited, next_dirs, cnt_move
flag = True
result = -1
while queue:
    idx1, idx2, v, d, c = queue.pop(0)
    for k in range(4):
        if visit[idx1][idx2][v][k] is False:
            visit[idx1][idx2][v][k] = True

            nxt1, nxt2 = idx1 + adj_list[d][k][0], idx2 + adj_list[d][k][1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] == '#':
                    continue
                if board[nxt1][nxt2] == '.':
                    queue.append((nxt1, nxt2, v, k, c + 1))
                    continue
                if board[nxt1][nxt2] == 1:
                    if v == 2:
                        result = c + 1
                        flag = False
                        break
                    else:
                        queue.append((nxt1, nxt2, 1, k, c + 1))
                elif board[nxt1][nxt2] == 2:
                    if v == 1:
                        result = c + 1
                        flag = False
                        break
                    else:
                        queue.append((nxt1, nxt2, 2, k, c + 1))

    if flag is False:
        break

print(result)
