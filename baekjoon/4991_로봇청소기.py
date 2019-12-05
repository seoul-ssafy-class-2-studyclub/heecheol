import collections
import itertools


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    board = [list(input()) for _ in range(h)]
    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    dusts = []
    d_num = 1

    for i in range(h):
        for j in range(w):
            if board[i][j] == '.' or board[i][j] == 'x':
                continue
            elif board[i][j] == '*':
                dusts.append((i, j))
                board[i][j] = d_num
                d_num += 1
            elif board[i][j] == 'o':
                board[i][j] = 0
                si, sj = i, j

    inf = float('inf')
    distance = [[inf] * d_num for _ in range(d_num)]

    for dust in dusts:
        oi, oj = dust
        board[oi][oj], temp = '.', board[oi][oj]
        queue = collections.deque([(oi, oj, 0)])
        visit = [[False] * w for _ in range(h)]

        while queue:
            idx1, idx2, m = queue.popleft()
            if visit[idx1][idx2] is False:
                visit[idx1][idx2] = True

                if board[idx1][idx2] == '.':
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < h and 0 <= nxt2 < w and visit[nxt1][nxt2] is False:
                            if board[nxt1][nxt2] == 'x':
                                continue
                            else:
                                queue.append((nxt1, nxt2, m + 1))
                else:
                    distance[temp][board[idx1][idx2]] = m
                    distance[board[idx1][idx2]][temp] = m
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < h and 0 <= nxt2 < w and visit[nxt1][nxt2] is False:
                            if board[nxt1][nxt2] == 'x':
                                continue
                            else:
                                queue.append((nxt1, nxt2, m + 1))

    perms = itertools.permutations(list(range(1, d_num)))
    min_value = inf

    for perm in perms:
        arr = [0] + list(perm)

        total = 0
        flag = False

        for i in range(d_num - 1):
            total += distance[arr[i]][arr[i + 1]]
            if min_value <= total:
                flag = True
                break

        if flag is True:
            continue
        else:
            min_value = total

    if min_value == inf:
        print(-1)
    else:
        print(min_value)
