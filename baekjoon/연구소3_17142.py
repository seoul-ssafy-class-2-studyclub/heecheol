import itertools
import collections
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board_init = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

virus = []
blanks_init = 0

for i in range(N):
    for j in range(N):
        if board_init[i][j] == 0:
            blanks_init += 1
        elif board_init[i][j] == 2:
            virus.append((i, j))

if blanks_init:
    combinations = itertools.combinations(virus, M)
    min_time = 9999

    for combination in combinations:
        queue = collections.deque(list(combination))

        board = [row[:] for row in board_init]
        blanks = blanks_init

        for r, c in combination:
            board[r][c] = 1

        seconds = 1
        flag = True

        while True:
            for _ in range(len(queue)):
                idx1, idx2 = queue.popleft()
                for adj in adj_list:
                    nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < N:
                        if board[nxt1][nxt2] == 0:
                            board[nxt1][nxt2] = 1
                            queue.append((nxt1, nxt2))
                            blanks -= 1
                        elif board[nxt1][nxt2] == 2:
                            board[nxt1][nxt2] = 1
                            queue.append((nxt1, nxt2))

            if blanks == 0:
                break
            elif seconds >= min_time:
                flag = False
                break
            elif queue:
                seconds += 1
            else:
                flag = False
                break

        if flag:
            min_time = seconds

    if min_time == 9999:
        print(-1)
    else:
        print(min_time)

else:
    print(0)
