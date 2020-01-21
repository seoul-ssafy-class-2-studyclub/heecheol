import heapq
import sys
sys.stdin = open('input.txt', 'r')


V, E, P = map(int, input().split())
adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

inf = float('inf')
distance = [inf] * (V + 1)

visit = [False] * (V + 1)
queue = []
heapq.heappush(queue, [0, 1, 1])

while queue:
    cnt, node, tf = heapq.heappop(queue)
    if node == V:
        break

    if visit[node] is False:
        visit[node] = True
        distance[node] = cnt
        if node == P:
            tf = 0
        for nxt, d in adj_list[node]:
            if visit[nxt] is False:
                heapq.heappush(queue, [cnt + d, nxt, tf])

if tf is 0:
    print('SAVE HIM')
else:
    print('GOOD BYE')