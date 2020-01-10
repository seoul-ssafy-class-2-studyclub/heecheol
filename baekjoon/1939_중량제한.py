import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
nodes = [{} for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    if nodes[A].get(B) is None:
        nodes[A][B] = nodes[B][A] = C
    else:
        if nodes[A][B] < C:
            nodes[A][B] = nodes[B][A] = C

start_node, end_node = map(int, input().split())

visit = [False] * (N + 1)
visit[start_node] = True

queue = []
for key, value in nodes[start_node].items():
    heapq.heappush(queue, (-value, key))

answer = float('inf')
flag = True
while True:
    possible_weight, island = heapq.heappop(queue)
    if visit[island] is True:
        continue
    visit[island] = True

    if -possible_weight < answer:
        answer = -possible_weight

    if island == end_node:
        break

    for key, value in nodes[island].items():
        if visit[key] is False:
            heapq.heappush(queue, (-value, key))

print(answer)
