from pprint import pprint
import sys
sys.stdin = open('input_1.txt', 'r')


def play(row, col, stone):
    board[row][col] = stone
    if stone == 1:
        arr = []
        for adj in adj_list:
            idx1 = row + adj[0]
            idx2 = col + adj[1]
            if 1 <= idx1 < N and 1 <= idx2 < N:
                if board[idx1][idx2] == 2:
                    # print(idx1, idx2)
                    arr2 = []
                    flag = False
                    while board[idx1][idx2] == 2:
                        arr2.append((idx1, idx2))
                        idx1 += adj[0]
                        idx2 += adj[1]
                        if idx1 < 1 or idx1 > N or idx2 < 1 or idx2 > N:
                            break
                        elif board[idx1][idx2] == 1:
                            flag = True
                            break
                        elif board[idx1][idx2] == 0:
                            break
                    if flag == True:
                        arr.extend(arr2)
        for idx in arr:
            board[idx[0]][idx[1]] = 1
    else:
        arr = []
        for adj in adj_list:
            idx1 = row + adj[0]
            idx2 = col + adj[1]
            if 1 <= idx1 <= N and 1 <= idx2 <= N:
                if board[idx1][idx2] == 1:
                    # print(idx1, idx2)
                    arr2 = []
                    flag = False
                    while board[idx1][idx2] == 1:
                        arr2.append((idx1, idx2))
                        idx1 += adj[0]
                        idx2 += adj[1]
                        if idx1 < 1 or idx1 > N or idx2 < 1 or idx2 > N:
                            break
                        elif board[idx1][idx2] == 2:
                            flag = True
                            break
                        elif board[idx1][idx2] == 0:
                            break
                    if flag == True:
                        arr.extend(arr2)
        for idx in arr:
            board[idx[0]][idx[1]] = 2


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*(N+1) for _ in range(N+1)]
    c = N//2
    board[c][c] = 2
    board[c+1][c+1] = 2
    board[c][c+1] = 1
    board[c+1][c] = 1

    adj_list = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

    for _ in range(M):
        r, c, s = map(int, input().split())
        play(r, c, s)
        # pprint(board)

    cnt_1 = 0
    cnt_2 = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if board[i][j] == 1:
                cnt_1 += 1
            elif board[i][j] == 2:
                cnt_2 += 1
    print('#{} {} {}'.format(tc, cnt_1, cnt_2))