import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    
    for _ in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)
    
    S, G = map(int, input().split())
    queue = [S]
    cnt = 0
    flag = 1
    while queue:
        cnt += 1
        queue2 = []
        while queue:
            node = queue.pop(0)
            if visited[node] == False:
                visited[node] = True
                if G in adj_list[node]:
                    queue2 = 0
                    flag = 0
                    break
                queue2.extend(adj_list[node])

        queue = queue2
    
    if flag == 1:
        print('#{} 0'.format(tc))
    else:
        print('#{} {}'.format(tc, cnt))
    


