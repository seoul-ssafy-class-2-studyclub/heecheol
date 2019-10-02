from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def checked(x, y, dx, dy):
    while True:
        x += dx
        y += dy
        if 0 <= x < N and 0 <= y < M:
            if board2[x][y] == 6:
                return
            elif board2[x][y] == 0:
                board2[x][y] = '#'
        else:
            return


def look(idx, board):
    global board2
    global min_zero
    if idx == c:
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt += 1
        # pprint(board)
        if cnt < min_zero:
            min_zero = cnt
            return

    else:
        x, y, n = cctv[idx]
        if n == 1:
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, 1)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, -1)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 1, 0)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, -1, 0)
            look(idx + 1, board2)

        elif n == 2:
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, 1)
            checked(x, y, 0, -1)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 1, 0)
            checked(x, y, -1, 0)
            look(idx + 1, board2)
        elif n == 3:
            #
            board2 = [row[:] for row in board]
            checked(x, y, -1, 0)
            checked(x, y, 0, 1)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, 1)
            checked(x, y, 1, 0)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 1, 0)
            checked(x, y, 0, -1)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, -1)
            checked(x, y, -1, 0)
            look(idx + 1, board2)
        elif n == 4:
            #
            board2 = [row[:] for row in board]
            checked(x, y, -1, 0)
            checked(x, y, 0, 1)
            checked(x, y, 1, 0)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, 1)
            checked(x, y, 1, 0)
            checked(x, y, 0, -1)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 1, 0)
            checked(x, y, 0, -1)
            checked(x, y, -1, 0)
            look(idx + 1, board2)
            #
            board2 = [row[:] for row in board]
            checked(x, y, 0, -1)
            checked(x, y, -1, 0)
            checked(x, y, 0, 1)
            look(idx + 1, board2)
        elif n == 5:
            board2 = [row[:] for row in board]
            checked(x, y, -1, 0)
            checked(x, y, 0, 1)
            checked(x, y, 1, 0)
            checked(x, y, 0, -1)
            look(idx + 1, board2)


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board2 = []
# dirs = [0, 4, 2, 4, 4, 1]
cctv = []
for i in range(N):
    for j in range(M):
        if 0 < board[i][j] < 6:
            cctv.append([i, j, board[i][j]])
c = len(cctv)
min_zero = 123456789
look(0, board)
print(min_zero)


#
# def rechecked(x, y, dx, dy):
#     while True:
#         x += dx
#         y += dy
#         if 0 <= x < N and 0 <= y < M:
#             if board[x][y] == 6:
#                 return
#             elif board[x][y] == '#':
#                 board[x][y] = 0
#         else:
#             return

