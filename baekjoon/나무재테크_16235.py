import sys
sys.stdin = open('input.txt', 'r')


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

board = [[5] * N for _ in range(N)]
adj_list = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

for _ in range(K):
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                trees[i][j].sort(reverse=True)
                died = 0
                for k in range(len(trees[i][j])-1, -1, -1):
                    if board[i][j] >= trees[i][j][k]:
                        board[i][j] -= trees[i][j][k]
                        trees[i][j][k] += 1
                    else:
                        age = trees[i][j].pop(k)
                        died += age // 2
                board[i][j] += died

    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                for age in trees[i][j]:
                    if age % 5 == 0:
                        for adj in adj_list:
                            nxt1, nxt2 = i + adj[0], j + adj[1]
                            if 0 <= nxt1 < N and 0 <= nxt2 < N:
                                trees[nxt1][nxt2].append(1)

            board[i][j] += A[i][j]

cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(trees[i][j])

print(cnt)
