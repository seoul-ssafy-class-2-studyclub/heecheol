from pprint import pprint
import copy

def rotation(board, N):
    rotated_board = copy.deepcopy(board)
    board = list(zip(*board))
    for i in range(N):
        for j in range(N):
            # clockwise
            rotated_board[i][j] = board[i][abs(N-j-1)]
            # countclockwise
            # rotated_board[i][j] = board[abs(N-i-1)][j]
    return rotated_board



for T in range(int(input())):
    board = []
    N = int(input())
    for n in range(N):
        row = list(input().split())
        board.append(row)
    pprint(board)

    board_90 = rotation(board, N)
    pprint(board_90)

    board_180 = rotation(board_90, N)
    pprint(board_180)

    board_270 = rotation(board_180, N)
    pprint(board_270)

    print(f'#{T+1}')
    for n in range(N):
        print(''.join(board_90[n]), ''.join(board_180[n]), ''.join(board_270[n]), )
        