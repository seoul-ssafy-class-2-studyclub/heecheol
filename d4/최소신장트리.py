import sys
sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())

    inf = float('inf')
    w_list = [[inf] * (V + 1) for _ in range(V + 1)]

    visit = [True] + [False] * V

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        w_list[n1][n2] = w
        w_list[n2][n1] = w

    cnt = 0
    sum_w = 0
    while cnt < V:
        min_w = 11
        for i in range(V + 1):
            if visit[i] is True:
                for j in range(V + 1):
                    if visit[j] is False and min_w > w_list[i][j]:
                        min_w = w_list[i][j]
                        start_node = i
                        next_node = j

        visit[next_node] = True
        sum_w += w_list[start_node][next_node]
        cnt += 1

    print('#{} {}'.format(tc, sum_w))



