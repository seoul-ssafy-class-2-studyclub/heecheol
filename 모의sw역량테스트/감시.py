# from pprint import pprint
# import sys
# sys.stdin = open('input.txt', 'r')

# CCTV 종류별 -> 방향별 체크
def in_cctv(board2, index):
    global min_cnt
    if index == number:
        cnt = 0
        for i0 in range(N):
            for j0 in range(M):
                if board2[i0][j0] == 0:
                    cnt += 1
        if min_cnt > cnt:
            min_cnt = cnt

    else:
        row, col = cctv_list[index]
        cctv_num = board2[row][col]

        if cctv_num == 1:
            for d in range(4):
                board = [r[:] for r in board2]

                if d == 0:  # 오른쪽방향
                    for c in range(1, M - col):
                        if board[row][col + c] == 6:
                            break
                        elif board[row][col + c] == 0:
                            board[row][col + c] = 7

                elif d == 1:    # 아래쪽
                    for r in range(1, N - row):
                        if board[row + r][col] == 6:
                            break
                        elif board[row + r][col] == 0:
                            board[row + r][col] = 7

                elif d == 2:    # 왼쪽
                    for c in range(1, col + 1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7

                else:   # 위쪽
                    for r in range(1, row + 1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7
                in_cctv(board, index+1)

        elif cctv_num == 2:
            for d in range(2):
                board = [r[:] for r in board2]

                if d == 0:  # 가로 방향
                    for c in range(1, M-col):
                        if board[row][col+c] == 6:
                            break
                        elif board[row][col+c] == 0:
                            board[row][col+c] = 7
                    for c in range(1, col + 1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7

                else:
                    for r in range(1, N-row):
                        if board[row+r][col] == 6:
                            break
                        elif board[row+r][col] == 0:
                            board[row+r][col] = 7
                    for r in range(1, row + 1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7
                in_cctv(board, index + 1)

        elif cctv_num == 3:
            for d in range(4):
                board = [r[:] for r in board2]

                if d == 0:  # 오른쪽 + 아래
                    for c in range(1, M-col):
                        if board[row][col+c] == 6:
                            break
                        elif board[row][col+c] == 0:
                            board[row][col+c] = 7
                    for r in range(1, N-row):
                        if board[row+r][col] == 6:
                            break
                        elif board[row+r][col] == 0:
                            board[row+r][col] = 7

                elif d == 1:  # 아래 + 왼쪽
                    for r in range(1, N - row):
                        if board[row + r][col] == 6:
                            break
                        elif board[row + r][col] == 0:
                            board[row + r][col] = 7
                    for c in range(1, col+1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7

                elif d == 2:  # 왼쪽 + 위쪽
                    for c in range(1, col+1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7
                    for r in range(1, row+1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7

                elif d == 3:  # 위쪽 + 오른쪽
                    for r in range(1, row+1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7
                    for c in range(1, N-col):
                        if board[row][col+c] == 6:
                            break
                        elif board[row][col+c] == 0:
                            board[row][col+c] = 7
                in_cctv(board, index + 1)

        elif cctv_num == 4:
            for d in range(4):
                board = [r[:] for r in board2]

                if d == 0:  # 오른쪽 + 아래 + 왼쪽
                    for c in range(1, M-col):
                        if board[row][col+c] == 6:
                            break
                        elif board[row][col+c] == 0:
                            board[row][col+c] = 7
                    for r in range(1, N-row):
                        if board[row+r][col] == 6:
                            break
                        elif board[row+r][col] == 0:
                            board[row+r][col] = 7
                    for c in range(1, col+1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7

                elif d == 1:  # 아래 + 왼쪽 + 위쪽
                    for r in range(1, N - row):
                        if board[row + r][col] == 6:
                            break
                        elif board[row + r][col] == 0:
                            board[row + r][col] = 7
                    for c in range(1, col+1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7
                    for r in range(1, row+1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7

                elif d == 2:  # 왼쪽 + 위쪽 + 오른쪽
                    for c in range(1, col+1):
                        if board[row][col - c] == 6:
                            break
                        elif board[row][col - c] == 0:
                            board[row][col - c] = 7
                    for r in range(1, row+1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7
                    for c in range(1, M - col):
                        if board[row][col + c] == 6:
                            break
                        elif board[row][col + c] == 0:
                            board[row][col + c] = 7

                elif d == 3:  # 위쪽 + 오른쪽 + 아래쪽
                    for r in range(1, row+1):
                        if board[row - r][col] == 6:
                            break
                        elif board[row - r][col] == 0:
                            board[row - r][col] = 7
                    for c in range(1, M-col):
                        if board[row][col+c] == 6:
                            break
                        elif board[row][col+c] == 0:
                            board[row][col+c] = 7
                    for r in range(1, N - row):
                        if board[row + r][col] == 6:
                            break
                        elif board[row + r][col] == 0:
                            board[row + r][col] = 7
                in_cctv(board, index + 1)

        elif cctv_num == 5:
            for _ in range(1):
                board = [r[:] for r in board2]
                # 위쪽 + 오른쪽 + 아래쪽 + 왼쪽
                for r in range(1, row + 1):
                    if board[row - r][col] == 6:
                        break
                    elif board[row - r][col] == 0:
                        board[row - r][col] = 7
                for c in range(1, M - col):
                    if board[row][col + c] == 6:
                        break
                    elif board[row][col + c] == 0:
                        board[row][col + c] = 7
                for r in range(1, N - row):
                    if board[row + r][col] == 6:
                        break
                    elif board[row + r][col] == 0:
                        board[row + r][col] = 7
                for c in range(1, col + 1):
                    if board[row][col - c] == 6:
                        break
                    elif board[row][col - c] == 0:
                        board[row][col - c] = 7
            in_cctv(board, index + 1)

# main
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 각 cctv 방향에 대한 경우의 수
directions = [0, 4, 2, 4, 4, 1]

# cctv 리스트
cctv_list = []
for i in range(N):
    for j in range(M):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv_list.append((i, j))
number = len(cctv_list)
min_cnt = 999999
in_cctv(board, 0)
print(min_cnt)
