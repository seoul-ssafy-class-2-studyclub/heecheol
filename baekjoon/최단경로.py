import sys
sys.stdin = open('input.txt', 'r')


def next_node():
    min_value = 3000000
    n_node = 0
    for i in range(1, V+1):
        if value[i] != 'INF' and visited[i] is False:
            if min_value > value[i]:
                min_value = value[i]
                n_node = i

    return n_node


V, E = map(int, input().split())
start_node = int(input())

graph = {i: {} for i in range(1, V+1)}
value = {i: 'INF' for i in range(1, V+1)}
value[start_node] = 0
visited = {i: False for i in range(1, V+1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u][v] = w

node = start_node
while node != 0:
    visited[node] = True
    cur_value = value[node]
    nxt_nodes = graph[node]
    for nxt_node in nxt_nodes.keys():
        new_value = cur_value + graph[node][nxt_node]
        if value[nxt_node] == 'INF' or new_value < value[nxt_node]:
            value[nxt_node] = new_value
    node = next_node()

for i in range(1, V+1):
    print(value[i])