import heapq
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

edges = []


for i in range(N - 1):
    for j in range(i + 1, N):
        heapq.heappush(edges, (board[i][j], i, j))

inf = float('inf')
new_board = [[inf] * N for _ in range(N)]
result = 0

while edges:
    v, s, e = heapq.heappop(edges)

    temp = []
    heapq.heappush(temp, inf)

    for k in range(N):
        if s == k or e == k:
            continue
        else:
            if new_board[s][k] == inf or new_board[s][k] == inf:
                continue
            heapq.heappush(temp, new_board[s][k] + new_board[k][e])
    tt = heapq.heappop(temp)
    if tt > v:
        result += v
        new_board[s][e] = new_board[e][s] = v
    else:
        new_board[s][e] = new_board[e][s] = tt

flag = True
for i in range(N - 1):
    for j in range(i + 1, N):
        if board[i][j] != new_board[i][j]:
            flag = False
            break
    if flag is False:
        break

if flag is False:
    print(-1)
else:
    print(result)
