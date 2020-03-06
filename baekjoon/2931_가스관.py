import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

for row in board:
    if 'M' in row:
        si = board.index(row)
        sj = row.index('M')
        break

# from Start
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # D => 0, 1, 2, 3
adj_pipe = [['|', '+', '1', '4'], ['-', '+', '3', '4'], ['|', '+', '2', '3'], ['-', '+', '1', '2']]

pipes = [
    {
        # up, D = 0
        '|': (-1, 0, 0),
        '+': (-1, 0, 0),
        '1': (0, 1, 1),
        '4': (0, -1, 3)
    },
    {
        # right, D= 1
        '-': (0, 1, 1),
        '+': (0, 1, 1),
        '3': (-1, 0, 0),
        '4': (1, 0, 2)
    },
    {
        # down, D = 2
        '|': (1, 0, 2),
        '+': (1, 0, 2),
        '2': (0, 1, 1),
        '3': (0, -1, 3)
    },
    {
        # left, D = 3
        '-': (0, -1, 3),
        '+': (0, -1, 3),
        '1': (1, 0, 2),
        '2': (-1, 0, 0)
    }
]

# find path
flag = False

for d in range(4):
    adj = adj_list[d]
    nxt1, nxt2 = si + adj[0], sj + adj[1]
    if 0 <= nxt1 < N and 0 <= nxt2 < M:
        if board[nxt1][nxt2] in adj_pipe[d]:
            idx1, idx2, D = nxt1, nxt2, d
            flag = True
            break

if flag is True:
    while True:
        di, dj, d_next = pipes[D][board[idx1][idx2]]
        nxt1, nxt2 = idx1 + di, idx2 + dj
        if board[nxt1][nxt2] == '.':
            break
        idx1, idx2 = nxt1, nxt2, pipes[d_next][board[nxt1][nxt2]][]

    pass

else:
    pass
