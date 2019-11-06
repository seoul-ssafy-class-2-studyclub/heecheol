import heapq
import sys
sys.stdin = open('input.txt', 'r')


V, E = map(int, input().split())

inf = float('inf')
dijkstra = [inf] * V

start = int(input()) - 1
dijkstra[start] = 0

board = [{} for _ in range(V)]
visit = [False] * V

for _ in range(E):
    u, v, w = map(int, input().split())
    if v - 1 in board[u - 1]:
        if board[u - 1][v - 1] > w:
            board[u - 1][v - 1] = w
    else:
        board[u - 1][v - 1] = w

queue = []
heapq.heappush(queue, (0, start))

while queue:
    w, v = heapq.heappop(queue)

    if visit[v] is False:
        visit[v] = True

        for key, value in board[v].items():
            if visit[key] is False:
                if w + value < dijkstra[key]:
                    dijkstra[key] = w + value
                    heapq.heappush(queue, (dijkstra[key], key))

for i in range(V):
    if dijkstra[i] == inf:
        print('INF')
    else:
        print(dijkstra[i])
