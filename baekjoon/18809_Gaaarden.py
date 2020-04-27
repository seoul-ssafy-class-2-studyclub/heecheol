import itertools
import collections
import sys
sys.stdin = open('input.txt', 'r')


N, M, R, G = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ground = []
answer = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            ground.append((i, j))

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

reds = itertools.combinations(ground, R)
for red in reds:
    rest = list(set(ground) - set(red))
    greens = itertools.combinations(rest, G)

    red_board = [row[:] for row in board]
    for ri, rj in list(red):
        red_board[ri][rj] = 3

    for green in greens:
        queue_red = collections.deque(red)
        queue_green = collections.deque(green)

        green_red_board = [row[:] for row in red_board]
        for gi, gj in list(green):
            green_red_board[gi][gj] = 4

        mark = 5

        flower_set = set()
        while queue_red and queue_green:

            for _ in range(len(queue_red)):
                idx1, idx2 = queue_red.popleft()
                for adj in adj_list:
                    nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if 1 <= green_red_board[nxt1][nxt2] <= 2:
                            green_red_board[nxt1][nxt2] = mark
                            queue_red.append((nxt1, nxt2))

            mark += 1

            for _ in range(len(queue_green)):
                idx1, idx2 = queue_green.popleft()
                for adj in adj_list:
                    nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if green_red_board[nxt1][nxt2] == mark - 1:
                            flower_set.add((nxt1, nxt2))
                            green_red_board[nxt1][nxt2] = 0
                        elif 1 <= green_red_board[nxt1][nxt2] <= 2:
                            green_red_board[nxt1][nxt2] = mark
                            queue_green.append((nxt1, nxt2))

            queue_red = collections.deque(list(set(queue_red) - flower_set))
            mark += 1

        if len(flower_set) > answer:
            answer = len(flower_set)

print(answer)
