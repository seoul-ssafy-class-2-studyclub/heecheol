from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def rotate(xx, dd, kk):
    for i in range(N // xx):
        row = xx * (i + 1) - 1
        if dd == 1:
            board[row] = board[row][kk:] + board[row][:kk]
        else:
            board[row] = board[row][M - kk:] + board[row][:M - kk]


def check_near(idx1, idx2, value):
    global flag

    for adj in adj_list:
        nxt1 = idx1 + adj[0]
        nxt2 = (idx2 + adj[1]) % M
        if 0 <= nxt1 < N and board[nxt1][nxt2] == value:
            flag = True
            board[nxt1][nxt2] = 'x'
            check_near(nxt1, nxt2, value)


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(T):
    x, d, k = map(int, input().split())
    rotate(x, d, k)

    flag_move = False   # 하나라도 바꾸는지
    for i in range(N):
        for j in range(M):
            if board[i][j] != 'x':
                temp = board[i][j]
                board[i][j] = 'x'
                flag = False
                check_near(i, j, temp)
                if flag is False:
                    board[i][j] = temp
                else:
                    flag_move = True

    if flag_move is False:
        avg = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 'x':
                    avg += board[i][j]
                    cnt += 1
        if cnt == 0:
            break
        else:
            avg /= cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j] != 'x':
                        if board[i][j] > avg:
                            board[i][j] -= 1
                        elif board[i][j] < avg:
                            board[i][j] += 1
# pprint(board)
result = 0
for i in range(N):
    for j in range(M):
        if board[i][j] != 'x':
            result += board[i][j]

print(result)