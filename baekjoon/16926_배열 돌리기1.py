# from pprint import pprint
import collections
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M, R = map(int, input().split())
board = [list(input().split()) for _ in range(N)]
new_board = [[0] * M for _ in range(N)]

B = min(N, M) // 2

orders = [collections.deque() for _ in range(B)]
idx_list = [collections.deque() for _ in range(B)]

adj_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for k in range(B):
    idx1 = idx2 = k

    idx_list[k].append((idx1, idx2))
    orders[k].append((board[idx1][idx2]))
    board[idx1][idx2] = 0

    for adj in adj_list:
        while True:
            idx1 += adj[0]
            idx2 += adj[1]
            if 0 <= idx1 < N and 0 <= idx2 < M:
                if board[idx1][idx2] == 0:
                    idx1 -= adj[0]
                    idx2 -= adj[1]
                    break
                else:
                    idx_list[k].append((idx1, idx2))
                    orders[k].append((board[idx1][idx2]))
                    board[idx1][idx2] = 0
            else:
                idx1 -= adj[0]
                idx2 -= adj[1]
                break

for i in range(B):
    rotateNum = R % len(orders[i])
    orders[i].rotate(rotateNum)

for i in range(B):
    for j in range(len(orders[i])):
        idx1, idx2 = idx_list[i][j]
        new_board[idx1][idx2] = orders[i][j]

# pprint(new_board)

answer = ['' for _ in range(N)]
for i in range(N):
    answer[i] = ' '.join(new_board[i])

print('\n'.join(answer))
