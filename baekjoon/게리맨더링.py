import itertools
import sys
sys.stdin = open('input.txt', 'r')


def is_continue(arr):
    if len(arr) > 1:
        vis = [False] * (N + 1)
        stack = [arr[0]]
        while stack:
            node = stack.pop()
            vis[node] = True
            for nxt in adj[node]:
                if nxt in arr and vis[nxt] is False:
                    stack.append(nxt)
        for n in arr:
            if vis[n] is False:
                return False

    o_arr = list(set(range(1, N + 1)) - set(arr))
    vis = [False] * (N + 1)
    stack = [o_arr[0]]
    while stack:
        node = stack.pop()
        vis[node] = True
        for nxt in adj[node]:
            if nxt in o_arr and vis[nxt] is False:
                stack.append(nxt)
    for n in o_arr:
        if vis[n] is False:
            return False
    return True


N = int(input())
population = list(map(int, input().split()))
total = sum(population)
adj = [[] for _ in range(N + 1)]
nxt_nodes = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    adj[i] = list(map(int, input().split()))
    nxt_nodes[i] = adj[i].pop(0)

result = 987654321
cities = list(range(1, N + 1))
flag = True
for i in range(1, N // 2 + 1):
    comb = list(itertools.combinations(cities, i))

    for part in comb:
        if is_continue(part) is True:
            partA = 0
            for j in list(part):
                partA += population[j - 1]
            if abs(total - 2 * partA) < result:
                result = abs(total - 2 * partA)
                if result == 0:
                    flag = False
                    break
    if flag is False:
        break

if result == 987654321:
    print(-1)
else:
    print(result)
