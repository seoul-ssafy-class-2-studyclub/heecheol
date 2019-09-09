import copy
from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

def sep(board):
    board_copy = copy.deepcopy(board)
    # print()
    # pprint(board_copy)
    cnt = 0
    for i in range(1, row-1):
        for j in range(1, col-1):
            if board_copy[i][j] != 0:
                stack=[(i, j)]
                while stack:
                    ix, iy = stack.pop()
                    board_copy[ix][iy] = 0
                    for ne in near:
                        if board_copy[ix+ne[0]][iy+ne[1]] != 0:
                            stack.append((ix+ne[0], iy+ne[1]))
                cnt += 1
    return cnt

# for문 2개 합치기

row, col = map(int, input().split())
board = [list(map(int, input().split())) for r in range(row)]
board2 = [[0]*col for r in range(row)]
near = [(-1, 0), (0, -1), (1, 0), (0, 1)]
count = sep(board)

year = 0

while count > 0:
    # board2 = [[0]*col for r in range(row)]
    for i in range(1, row-1):
        for j in range(1, col-1):
            zeros = 0
            if board[i][j] != 0:                
                for ne in near:
                    if board[i+ne[0]][j+ne[1]] == 0:
                        zeros += 1
            board2[i][j] = zeros
    # print('#')
    # pprint(board2)
    
    for i in range(1, row-1):
        for j in range(1, col-1):
            value = board[i][j] - board2[i][j]
            if value <= 0:
                board[i][j] = 0
            else:
                board[i][j] = value
    
    year += 1
    
    count = sep(board)
    if count > 1:
        break

print(year)
