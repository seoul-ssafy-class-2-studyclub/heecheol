import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
company = [-1] * N
for i in range(N):
    company[i] = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
inf = float('inf')
dp = [(inf, inf) for _ in range(N)]
dp[0] = (0, 0)

queue = []
heapq.heappush(queue, (0, 0, 0))

while queue:
    tr, time, cur = heapq.heappop(queue)
    # print(cur)
    # print(dp)

    if cur == M:
        # print(dp[M])
        break

    for n in range(N):

        if board[cur][n] == 0:
            continue

        if company[cur] != company[n]:
            if dp[n][0] < tr + 1:
                continue

            n_time = time + board[cur][n]
            if dp[n][0] == tr + 1 and dp[n][1] <= n_time:
                continue

            else:
                dp[n] = (tr + 1, n_time)
                heapq.heappush(queue, (tr + 1, n_time, n))

        else:
            if dp[n][0] < tr:
                continue

            n_time = time + board[cur][n]
            if dp[n][0] == tr and dp[n][1] <= n_time:
                continue

            else:
                dp[n] = (tr, n_time)
                heapq.heappush(queue, (tr, n_time, n))

print(tr, time)
