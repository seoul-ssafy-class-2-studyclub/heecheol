import heapq
import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


V, E, P = map(int, input().split())
adj_list = [(0, 0) for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

queue = []
heapq.heappush(queue, (0, 1, [False] * (V + 1)))
total = float('inf')
result = 'GOOD BYE'
while True:
    distance, node, vis = heapq.heappop(queue)
    if distance > total:
        break
    if vis[P] is True:
        result = 'SAVE HIM'
    if distance ==

    for nxt, value in adj_list[node]:
        if vis[nxt] is False:
            visit = vis[:]
            visit[nxt] = True
            heapq.heappush(queue, (distance + value, nxt, visit))


