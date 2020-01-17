import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

idx_three = [[(0, 1), (1, 0), (0, 0)], [(1, 1), (1, 0), (0, 0)], [(1, 1), (0, 1), (0, 0)], [(1, 1), (1, 0), (0, 1)]]
idx_one = [[(-1, 0), (-1, 1), (0, 2), (1, 1), (2, 0), (1, -1), (0, -1)], [(-1, 0), (1, 2), (2, 1), (1, -1), (0, -1)], [(0, -1), (-1, 1), (2, 1)], [(1, -1), (-1, 1)]]

result = 0

for r in range(N):
    for c in range(M):

        for i in range(4):
            temp3 = 0
            flag = True
            for adj in idx_three[i]:
                nxt1, nxt2 = r + adj[0], c + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    temp3 += board[nxt1][nxt2]
                else:
                    flag = False
                    break
            if flag:
                for adj in idx_one[i]:
                    nxt1, nxt2 = r + adj[0], c + adj[1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if temp3 + board[nxt1][nxt2] > result:
                            result = temp3 + board[nxt1][nxt2]
                            # print(result, r, c, i)
                    else:
                        continue

        if r + 3 < N:
            temp4 = 0
            for dr in range(4):
                temp4 += board[r + dr][c]
            if temp4 > result:
                result = temp4
        if c + 3 < M:
            temp4 = 0
            for dc in range(4):
                temp4 += board[r][c + dc]
            if temp4 > result:
                result = temp4

print(result)
