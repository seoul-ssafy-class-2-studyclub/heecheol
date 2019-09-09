import sys
import time
import copy
from pprint import pprint
sys.stdin = open('input.txt', 'r')


def zeros(i, j):
    
    near = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for a, b in near:
        if new_board[i + a][j + b] != 0:
            new_board[i + a][j + b] = '-'
        else:
            new_board[i][j] = '-'
            zeros(i+a, j+b)


for tc in range(int(input())):

    N = int(input())
    # make (N+2)*(N+2) board
    
    board =[]
    board.append(['-'] * (N+2))
    for n in range(N):    
        board.append(['-'] + list(input()) + ['-'])
    board.append(['-'] * (N+2))


    # new board
    new_board = copy.deepcopy(board)
    near = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            
            if board[i][j] != '*':
                count = 0
                for a, b in near:
                    if board[i + a][j + b] == '*':
                        count += 1
                new_board[i][j] = count
            else:
                new_board[i][j] = '-'
                

    for i in range(1, N+1):
        for j in range(1, N+1):
            if new_board[i][j] == 0:
                zeros(i, j)

    count = 0
    for i in range(1, N+1):
        for element in new_board[i]:
            if element != '-':
                count += 1

    print(f'#{tc + 1} {count}')
    