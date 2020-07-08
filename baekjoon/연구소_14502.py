import itertools
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [input().split() for _ in range(N)]

virus = []
blanks = []
number_of_blanks = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            blanks.append((i, j))
            number_of_blanks += 1
        elif board[i][j] == '2':
            virus.append((i, j))

adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
spread = float('inf')

for new_wall in list(itertools.combinations(blanks, 3)):
    copied_board = [row[:] for row in board]
    for x, y in new_wall:
        copied_board[x][y] = '1'
    queue = virus[:]
    cnt = 0
    while queue:
        idx1, idx2 = queue.pop(0)
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if copied_board[nxt1][nxt2] == '0':
                    copied_board[nxt1][nxt2] = '2'
                    queue.append((nxt1, nxt2))
                    cnt += 1
        if cnt >= spread:
            break

    if cnt < spread:
        spread = cnt

print(number_of_blanks - spread - 3)
