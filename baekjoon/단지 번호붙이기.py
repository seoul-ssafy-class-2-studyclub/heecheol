import sys
sys.stdin = open('input.txt', 'r')


def connect(ix, iy):
    stack = [(ix, iy)]
    cnt = 0
    while len(stack) > 0:
        i, j = stack.pop()
        if board[i][j] != '0':
            board[i][j] = '0'
            cnt += 1
            if 1 <= i < N-1 and 1 <= j < N-1:
                near = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif i == 0 and j == 0:
                near = [(1, 0), (0, 1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif 1<= i < N-1 and j == 0:
                near = [(-1, 0), (1, 0), (0, 1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif 1<= i < N-1 and j == N-1:
                near = [(-1, 0), (1, 0), (0, -1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif i==0 and 1 <= j < N-1:
                near = [(1, 0), (0, 1), (0, -1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif i==N-1 and 1 <= j < N-1:
                near = [(-1, 0), (0, -1), (0, 1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif i == 0 and j == N-1:
                near = [(1, 0), (0, -1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            elif i == N-1 and j == 0:
                near = [(-1, 0), (0, 1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
            else:
                near = [(-1, 0), (0, -1)]
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == '1':
                        stack.append((i+ne[0], j+ne[1]))
    print(cnt)                


N = int(input())
board = [list(input()) for i in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            connect(i, j)