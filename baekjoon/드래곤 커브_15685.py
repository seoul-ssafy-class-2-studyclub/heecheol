from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def init(xx, yy, dd):
    if dd == 0:
        return [(xx, yy), (xx+1, yy)]
    elif dd == 1:
        return [(xx, yy), (xx, yy-1)]
    elif dd == 2:
        return [(xx, yy), (xx-1, yy)]
    else:
        return [(xx, yy), (xx, yy+1)]


def rotate():
    end_x, end_y = dragon_curve[-1]
    for i in range(len(dragon_curve) - 2, -1, -1):
        idx1, idx2 = dragon_curve[i][0] - end_x, dragon_curve[i][1] - end_y
        nxt1, nxt2 = -idx2 + end_x, idx1 + end_y
        if 0 <= nxt1 <= 100 and 0 <= nxt2 <= 100:
            dragon_curve.append((nxt1, nxt2))


def paint_board():
    for j, i in dragon_curve:
        board[i][j] = 1


N = int(input())
board = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon_curve = init(x, y, d)
    for _ in range(g):
        rotate()
    paint_board()

cnt = 0
for r in range(100):
    for c in range(100):
        if board[r][c] == 1:
            if board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
                cnt += 1

print(cnt)
