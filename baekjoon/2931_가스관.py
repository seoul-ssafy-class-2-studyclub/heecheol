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
        if board[nxt1][nxt2] == '.':
            continue
        if board[nxt1][nxt2] in adj_pipe[d]:
            idx1, idx2, D = nxt1, nxt2, d
            flag = True
            break

if flag is True:
    while True:
        di, dj, D = pipes[D][board[idx1][idx2]]
        idx1 += di
        idx2 += dj
        if board[idx1][idx2] == '.':
            break

    # 빈칸 발견 이후
    flag_z = False
    for p in adj_pipe[D]:
        board[idx1][idx2] = p
        di, dj, nd = pipes[D][p]
        nxt1, nxt2 = idx1 + di, idx2 + dj
        if 0 <= nxt1 < N and 0 <= nxt2 < M:
            if board[nxt1][nxt2] == '.':
                continue
            if board[nxt1][nxt2] in adj_pipe[nd]:
                while True:
                    di, dj, nd = pipes[nd][board[nxt1][nxt2]]
                    nxt1 += di
                    nxt2 += dj
                    if board[nxt1][nxt2] == 'Z':
                        print(idx1 + 1, idx2 + 1, p)
                        flag_z = True
                        break
                    if board[nxt1][nxt2] not in adj_pipe[nd]:
                        break
                if flag_z is True:
                    break
    else:
        board[idx1][idx2] = '.'
        for p in adj_pipe[D]:
            if p == '+':
                continue
            di, dj, nd = pipes[D][p]
            nxt1, nxt2 = idx1 + di, idx2 + dj
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] == 'Z':
                    print(idx1 + 1, idx2 + 1, p)
                    break

else:
    flag_z = False
    for d in range(4):
        adj = adj_list[d]
        idx1, idx2 = si + adj[0], sj + adj[1]
        if 0 <= idx1 < N and 0 <= idx2 < M:
            for p in adj_pipe[d]:
                board[idx1][idx2] = p
                di, dj, nd = pipes[d][p]
                nxt1, nxt2 = idx1 + di, idx2 + dj
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board[nxt1][nxt2] in adj_pipe[nd]:
                        while True:
                            di, dj, nd = pipes[nd][board[nxt1][nxt2]]
                            nxt1 += di
                            nxt2 += dj
                            if board[nxt1][nxt2] == 'Z':
                                print(idx1 + 1, idx2 + 1, p)
                                flag_z = True
                                break
                            if board[nxt1][nxt2] not in adj_pipe[nd]:
                                break
                        if flag_z is True:
                            break
            else:
                board[idx1][idx2] = '.'

            if flag_z is True:
                break
    else:
        for d in range(4):
            adj = adj_list[d]
            idx1, idx2 = si + adj[0], sj + adj[1]
            if 0 <= idx1 < N and 0 <= idx2 < M:
                if board[idx1][idx2] != '.':
                    continue

                for p in adj_pipe[d]:
                    di, dj, nd = pipes[d][p]
                    nxt1, nxt2 = idx1 + di, idx2 + dj
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if board[nxt1][nxt2] == 'Z':
                            print(idx1 + 1, idx2 + 1, p)
                            flag_z = True
                            break

                if flag_z is True:
                    break
