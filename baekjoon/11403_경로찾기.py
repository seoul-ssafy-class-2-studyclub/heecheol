from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def find_route(idx):
    queue = []

    for i in range(N):
        if board[idx][i] == '1':
            queue.append(i)

    idx_q = 0
    while idx_q != len(queue):
        nxt = queue[idx_q]
        idx_q += 1

        if nxt == idx:
            continue

        elif visit[nxt] is True:
            for i in range(N):
                if board[nxt][i] == '1':
                    board[idx][i] = '1'

        else:
            for j in range(N):
                if board[nxt][j] == '1' and j not in queue:
                    board[idx][j] = '1'
                    queue.append(j)


N = int(input())
board = [input().split() for _ in range(N)]
visit = [False] * N

for i in range(N):
    find_route(i)
    visit[i] = True


for row in board:
    print(' '.join(row))
