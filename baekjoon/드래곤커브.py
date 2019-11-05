from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())

board = [[-1] * 15 for _ in range(15)]

for n in range(N):
    j, i, d, g = map(int, input().split())
    points = collections.deque()
    points.append((j, i))   # y좌표, x좌표
    if d == 0:
        points.append((j, i + 1))
    elif d == 1:
        points.append((j - 1, i))
    elif d == 2:
        points.append((j, i - 1))
    else:
        points.append((j + 1, i))

    for _ in range(1, g):
        yy, xx = points[-1]
        for ii in range(len(points)):
            py, px = points[ii]
            ny, nx = px - xx + yy, xx + yy - py
            if 0 <= nx < 101 and 0 <= ny < 101:
                points.append((ny, nx))

    for point in points:
        j, i = point[0], point[1]
        board[j][i] = 0

cnt = 0
for i in range(15):
    for j in range(15):
        if board[i][j] == 0:
            if board[i + 1][j] == 0 and board[i][j + 1] == 0 and board[i + 1][j + 1] == 0:
                cnt += 1

print(cnt)
pprint(board)