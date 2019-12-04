from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
left = [(0, -1), (-1, 0), (0, 1), (1, 0)]
back = {
    0: (1, 0),
    1: (0, -1),
    2: (-1, 0),
    3: (0, 1)
}
cnt = 0
flag = True
while flag:
    board[r][c] = 2
    cnt += 1
    n = 0
    while True:
        nxt1, nxt2 = r + left[d][0], c + left[d][1]
        if n == 4:
            nr, nc = r + back[d][0], c + back[d][1]
            if board[nr][nc] == 1:
                flag = False
                break
            else:
                r, c = nr, nc
                n = 0
                continue
        else:
            d = (d + 3) % 4
            n += 1
            if board[nxt1][nxt2] == 0:
                r, c = nxt1, nxt2
                break
print(cnt)