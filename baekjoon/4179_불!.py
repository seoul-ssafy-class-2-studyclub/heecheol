import collections
import sys
sys.stdin = open('input.txt', 'r')


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

jihun = collections.deque()
fire = collections.deque()

for i in range(R):
    for j in range(C):
        if board[i][j] == '.' or board[i][j] == '#':
            continue
        elif board[i][j] == 'F':
            fire.append((i, j))
        else:
            jihun.append((i, j))

flag = False    # finish
cnt = 0
while jihun:
    cnt += 1
    for i in range(len(jihun)):
        idx1, idx2 = jihun.popleft()
        if board[idx1][idx2] == 'J':
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < R and 0 <= nxt2 < C:
                    if board[nxt1][nxt2] == '.':
                        board[nxt1][nxt2] = 'J'
                        jihun.append((nxt1, nxt2))
                else:
                    flag = True
                    break
            if flag is True:
                break
    if flag is True:
        break

    for i in range(len(fire)):
        idx1, idx2 = fire.popleft()
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < R and 0 <= nxt2 < C:
                if board[nxt1][nxt2] == '.' or board[nxt1][nxt2] == 'J':
                    board[nxt1][nxt2] = 'F'
                    fire.append((nxt1, nxt2))

if flag is True:
    print(cnt)
else:
    print('IMPOSSIBLE')
