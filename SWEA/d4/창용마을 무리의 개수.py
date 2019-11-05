import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    nodes = [[] for _ in range(N + 1)]

    for _ in range(M):
        p1, p2 = map(int, input().split())
        nodes[p1].append(p2)
        nodes[p2].append(p1)
    # print(nodes)
    cnt = 0
    visited = [True] + [False] * N
    for i in range(1, N + 1):
        if not visited[i]:
            stack = [i]
            while stack:
                nxt_node = stack.pop()
                if visited[nxt_node] is False:
                    visited[nxt_node] = True
                    stack += nodes[nxt_node]
                # nodes[nxt_node] = []
            cnt += 1
    print('#{} {}'.format(tc, cnt))

