import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')


def chk(idx1, idx2, value):
    board2[idx1][idx2] = '.'

    for adj in adj_list:
        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
        if 0 <= nxt1 < 12 and 0 <= nxt2 < 6:
            if board2[nxt1][nxt2] == value:
                arr.append((nxt1, nxt2))
                chk(nxt1, nxt2, value)


board = [list(input()) for _ in range(12)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0
while True:
    # pprint(board)
    erased = False
    board2 = [row[:] for row in board]

    for i in range(12):
        for j in range(6):
            if board2[i][j] != '.':
                arr = [(i, j)]
                chk(i, j, board2[i][j])
                if len(arr) >= 4:
                    erased = True
                    for point in arr:
                        ix, iy = point
                        board[ix][iy] = '.'

    if erased is True:
        cnt += 1
        for j in range(6):
            for i1 in range(11):
                if board[i1][j] != '.':
                    for i2 in range(i1 + 1, 12):
                        if board[i2][j] == '.':
                            board[i1][j], board[i2][j] = board[i2][j], board[i1][j]
                            break
    else:
        break

print(cnt)
