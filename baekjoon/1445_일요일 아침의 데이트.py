from pprint import pprint
import heapq
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

# heapq (garbage, near, idx1, idx2)
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
garbage = []
queue = []

for i in range(N):
    for j in range(M):
        if board[i][j] == '.' or board[i][j] == 'n':
            continue
        if board[i][j] == 'g':
            for adj in adj_list:
                nxt1, nxt2 = i + adj[0], j + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board[nxt1][nxt2] == '.':
                        board[nxt1][nxt2] = 'n'
            continue

        if board[i][j] == 'S':
            si, sj = i, j
            heapq.heappush(queue, (0, 0, si, sj))
            continue

inf = float('inf')
dp = [[(inf, inf)] * M for _ in range(N)]
flag = False

while queue:
    g, n, idx1, idx2 = heapq.heappop(queue)
    if dp[idx1][idx2][0] < g:
        continue

    elif dp[idx1][idx2][0] == g and dp[idx1][idx2][1] <= n:
        continue

    else:
        dp[idx1][idx2] = (g, n)
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] == '.':
                    heapq.heappush(queue, (g, n, nxt1, nxt2))
                elif board[nxt1][nxt2] == 'n':
                    heapq.heappush(queue, (g, n + 1, nxt1, nxt2))
                elif board[nxt1][nxt2] == 'g':
                    heapq.heappush(queue, (g + 1, n, nxt1, nxt2))
                elif board[nxt1][nxt2] == 'F':
                    flag = True
                    break
        if flag is True:
            break

print(g, n)






