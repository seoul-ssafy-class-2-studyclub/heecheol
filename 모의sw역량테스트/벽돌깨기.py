from pprint import pprint
import copy
import sys
sys.stdin = open('input.txt', 'r')


def crash(ix, iy):
    if board[ix][iy] == 1:
        board[ix][iy] = 0    
    else:
        power = board[ix][iy]
        board[ix][iy] = 0
        for p in range(1, power):
            # up (row)
            u_ix = ix + p          
            if 0 <= u_ix < H and 0 <= iy < W and board[u_ix][iy] != 0:
                crash(u_ix, iy)
            # down (row)
            d_ix = ix - p
            if 0 <= d_ix < H and 0 <= iy < W and board[d_ix][iy] != 0:
                crash(d_ix, iy)
            # right (col)
            r_iy = iy + p
            if 0 <= ix < H and 0 <= r_iy < W and board[ix][r_iy] != 0:
                crash(ix, r_iy)
            # left (col)
            l_iy = iy - p
            if 0 <= ix < H and 0 <= l_iy < W and board[ix][l_iy] != 0:
                crash(ix, l_iy)


def arrange():
    for col in range(W):
        for i in range(9, 0, -1):
            if board[i][col] == 0:
                for j in range(i-1, -1, -1):
                    if board[j][col] != 0:
                        board[i][col], board[j][col] = board[j][col], board[i][col]
                        break
                else:
                    break


def drop(shoot, board):
    if shoot == N-1:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if board[i][j] != 0:
                    cnt += 1
        cnt_list.append(cnt)

    else:
        for col in range(W):
            board = copy.deepcopy(board)
            for row in range(H):
                if board[row][col] != 0:                    
                    crash(row, col)
                    arrange()                    
                    drop(shoot+1, board)
                    break

                        

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    
    shoot = 0
    cnt_list = []
    drop(shoot, board)

    print(cnt_list)