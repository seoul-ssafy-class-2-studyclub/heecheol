import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
r, c, d = map(int, input().split())
board = [input().split() for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cnt = 0
flag = True
while flag:
    # step0
    if board[r][c] == '0':
        board[r][c] = '2'
        cnt += 1

    # step1
    for k in range(4):
        look = (d - 1 - k) % 4
        nxt1, nxt2 = r + adj_list[look][0], c + adj_list[look][1]
        if 0 <= nxt1 < N and 0 <= nxt2 < M:
            if board[nxt1][nxt2] == '0':
                r, c, d = nxt1, nxt2, look
                break
    else:
        look = (d - 2) % 4
        nxt1, nxt2 = r + adj_list[look][0], c + adj_list[look][1]
        if 0 <= nxt1 < N and 0 <= nxt2 < M:
            if board[nxt1][nxt2] == '2':
                r, c = nxt1, nxt2
            else:
                flag = False
        else:
            flag = False

print(cnt)
