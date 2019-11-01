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
    for adj in adj_list:
        nxt1 = idx1 + adj[0]
        nxt2 = (idx2 + adj[1] + M) % M
        if 0 <= nxt1 < N and board[nxt1][nxt2] == value:
            board[nxt1][nxt2] = 0
            check_near(nxt1, nxt2, value)


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# pprint(board)

for _ in range(T):
    # print('-')
    x, d, k = map(int, input().split())
    rotate(x, d, k)
    # pprint(board)
    flag_move = False
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                temp = board[i][j]
                for adj in adj_list:
                    n1, n2 = i + adj[0], (j + adj[1]) % M
                    if 0 <= n1 < N and board[n1][n2] == temp:
                        board[i][j] = 0
                        check_near(i, j, temp)
                        flag_move = True
                        break
    # pprint(board)
    if flag_move is False:
        # print('*')
        total = 0
        cnt = M * N
        for i in range(N):
            total += sum(board[i])
            cnt -= board[i].count(0)

        if cnt <= 1:
            continue
        else:
            avg = total / cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j]:
                        if board[i][j] > avg:
                            board[i][j] -= 1
                        elif board[i][j] < avg:
                            board[i][j] += 1
        # pprint(board)
result = 0
for i in range(N):
    result += sum(board[i])

print(result)
