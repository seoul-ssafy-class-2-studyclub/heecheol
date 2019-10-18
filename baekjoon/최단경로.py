import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
K = int(input()) - 1

inf = float('inf')
board = [[inf] * V for _ in range(V)]
for i in range(V):
    board[i][i] = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    board[u - 1][v - 1] = w

nxt = 0
while True:
    if nxt == V - 1:
        break


for k in range(V):
    for i in range(V):
        if i != k and board[i][k] != inf:
            for j in range(V):
                if j != k and j != i and board[k][j] != inf:
                    board[i][j] = min(board[i][j], board[i][k] + board[k][j])

for i in range(V):
    print(board[K][i])