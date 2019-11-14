from pprint import pprint
import collections
import itertools
import sys
sys.stdin = open('input.txt', 'r')


def spread():
    queue = collections.deque(virus)
    while queue:
        idx1, idx2 = queue.popleft()
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board2[nxt1][nxt2] == 0:
                    queue.append((nxt1, nxt2))
                    board2[nxt1][nxt2] = 2


def check():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if board2[i][j] == 0:
                cnt += 1
    return cnt


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = 0
blank = []
virus = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            blank.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

wall_positions = list(itertools.combinations(blank, 3))
for walls in wall_positions:
    board2 = [row[:] for row in board]
    for wall in walls:
        i, j = wall
        board2[i][j] = 1
    spread()
    count = check()
    if count > result:
        # pprint(board2)
        result = count

print(result)

