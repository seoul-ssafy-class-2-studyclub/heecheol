import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
company = [-1] * N
for i in range(N):
    company[i] = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

visit = [False] * N
visit[0] = True
transfer_min = 987654321
min_time = 987654321
queue = []
heapq.heappush(queue, (0, 0, 0, visit[:]))

while queue:
    t_cnt, time, cur, vis = heapq.heappop(queue)

    if cur == M:
        if min_time > time:
            transfer_min = t_cnt
            min_time = time
            break

    for nxt in range(N):
        if board[cur][nxt] > 0 and vis[nxt] is False:
            n_vis = vis[:]
            n_vis[nxt] = True
            if company[cur] != company[nxt]:
                heapq.heappush(queue, (t_cnt + 1, time + board[cur][nxt], nxt, n_vis))
            else:
                heapq.heappush(queue, (t_cnt, time + board[cur][nxt], nxt, n_vis))

print(transfer_min, min_time)
