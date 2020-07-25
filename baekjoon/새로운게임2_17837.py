from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def white(i1, i2, n1, n2, n):
    idx = on_board[i1][i2].index(n)
    for _ in range(len(on_board[i1][i2][idx:])):
        h = on_board[i1][i2].pop(idx)
        on_board[n1][n2].append(h)
        indexes[h] = (n1, n2)


def red(i1, i2, n1, n2, n):
    idx = on_board[i1][i2].index(n)
    for _ in range(len(on_board[i1][i2][idx:])):
        h = on_board[i1][i2].pop()
        on_board[n1][n2].append(h)
        indexes[h] = (n1, n2)


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

on_board = [[[] for _ in range(N)] for __ in range(N)]
indexes = [(0, 0)] * K
direction = [0] * K

for k in range(K):
    r, c, d = map(int, input().split())
    on_board[r-1][c-1].append(k)
    indexes[k] = (r-1, c-1)
    direction[k] = d-1

adj_list = [(0, 1), (0, -1), (-1, 0), (1, 0)]
next_dir = {0: 1, 1: 0, 2: 3, 3: 2}

turn = 0
flag = False
while turn < 1000:
    turn += 1
    for k in range(K):
        idx1, idx2 = indexes[k]
        nxt1, nxt2 = idx1 + adj_list[direction[k]][0], idx2 + adj_list[direction[k]][1]

        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if board[nxt1][nxt2] == 0:
                white(idx1, idx2, nxt1, nxt2, k)
            elif board[nxt1][nxt2] == 1:
                red(idx1, idx2, nxt1, nxt2, k)
            else:
                nxt1, nxt2 = idx1 - adj_list[direction[k]][0], idx2 - adj_list[direction[k]][1]
                direction[k] = next_dir[direction[k]]
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if board[nxt1][nxt2] == 2:
                        continue
                    elif board[nxt1][nxt2] == 0:
                        white(idx1, idx2, nxt1, nxt2, k)
                    else:
                        red(idx1, idx2, nxt1, nxt2, k)
                else:
                    continue

        else:
            nxt1, nxt2 = idx1 - adj_list[direction[k]][0], idx2 - adj_list[direction[k]][1]
            direction[k] = next_dir[direction[k]]
            if board[nxt1][nxt2] == 2:
                continue
            elif board[nxt1][nxt2] == 0:
                white(idx1, idx2, nxt1, nxt2, k)
            else:
                red(idx1, idx2, nxt1, nxt2, k)

        if len(on_board[nxt1][nxt2]) >= 4:
            flag = True
            break

    if flag:
        break

if flag:
    print(turn)
else:
    print(-1)
