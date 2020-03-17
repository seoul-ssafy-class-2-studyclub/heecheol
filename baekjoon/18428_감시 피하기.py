import itertools
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [input().split() for _ in range(N)]

blanks = []
teachers = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'S':
            continue
        elif board[i][j] == 'T':
            teachers.append((i, j))
        else:
            blanks.append((i, j))

adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for obstacles in itertools.combinations(list(range(len(blanks))), 3):
    for i in obstacles:
        obs = blanks[i]
        board[obs[0]][obs[1]] = 'O'

    flag = True
    for idx1, idx2 in teachers:
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            while True:
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if board[nxt1][nxt2] == 'O':
                        break
                    if board[nxt1][nxt2] == 'S':
                        flag = False
                        break
                    nxt1 += adj[0]
                    nxt2 += adj[1]
                else:
                    break
            if flag is False:
                break
        if flag is False:
            break

    if flag is False:
        for i in obstacles:
            obs = blanks[i]
            board[obs[0]][obs[1]] = 'X'
        continue
    else:
        print('YES')
        break
else:
    print('NO')
