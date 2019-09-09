import sys
sys.stdin = open('input.txt', 'r')


def boundary(ix, iy):
    stack = [(ix, iy)]
    union = []
    while stack:
        idx1, idx2 = stack.pop()
        if visited[idx1][idx2] is False:
            visited[idx1][idx2] = True
            union.append((idx1, idx2))

            for adj in adj_list:
                nxt1 = idx1 + adj[0]
                nxt2 = idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N and visited[nxt1][nxt2] is False:
                    if L <= abs(board[nxt1][nxt2] - board[idx1][idx2]) <= R:
                        stack.append((nxt1, nxt2))

    population = 0
    if len(union) > 1:
        for idx in union:
            r, c = idx[0], idx[1]
            population += board[r][c]
        people = population // len(union)
        for idx in union:
            r, c = idx[0], idx[1]
            board[r][c] = people


# main
N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # 상 우 하 좌

move = 0
while True:
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] is False:
                boundary(i, j)
                cnt += 1
    move += 1
    if cnt == N**2:
        break
print(move-1)

