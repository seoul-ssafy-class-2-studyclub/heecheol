import sys
sys.stdin = open('input.txt', 'r')


def find_group(x, y, m):
    sum_population = cnt_group = 0

    queue = [(x, y)]
    while queue:
        idx1, idx2 = queue.pop(0)
        cnt_group += 1
        sum_population += population[idx1][idx2]

        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < N:
                if board[nxt1][nxt2] == 0:
                    if L <= abs(population[nxt1][nxt2] - population[idx1][idx2]) <= R:
                        board[nxt1][nxt2] = m
                        queue.append((nxt1, nxt2))

    return sum_population // cnt_group


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]
move = 0

while True:
    board = [[0] * N for _ in range(N)]
    mark = 0
    group = {}

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                mark += 1
                board[i][j] = mark
                average = find_group(i, j, mark)
                group[mark] = average

    if mark == N ** 2:
        break

    for i in range(N):
        for j in range(N):
            population[i][j] = group[board[i][j]]

    move += 1

print(move)
