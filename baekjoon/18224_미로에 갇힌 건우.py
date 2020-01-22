import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]
visit = [[False] * N for _ in range(N)]
queue = [[0, 0, True, 0, 1]]
arrived = False
while queue:
    idx1, idx2, is_sun, m, day = queue.pop(0)

    if m == 0 or m % M != 0:
        pass
    else:
        if is_sun is True:
            is_sun = False
        else:
            day += 1
            is_sun = True
    # print()
    # print(idx1, idx2, is_sun)
    if idx1 == idx2 == N - 1:
        arrived = True
        break

    if visit[idx1][idx2] is False:
        visit[idx1][idx2] = True

        # print(idx1, idx2, m, is_sun)
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < N:
                if visit[nxt1][nxt2] is True:
                    continue
                elif board[nxt1][nxt2] == 0:
                    queue.append([nxt1, nxt2, is_sun, m + 1, day])
                else:
                    if is_sun is True:
                        continue

                    while True:
                        nxt1, nxt2 = nxt1 + adj[0], nxt2 + adj[1]
                        if 0 <= nxt1 < N and 0 <= nxt2 < N:
                            if board[nxt1][nxt2] == 1:
                                continue
                            else:
                                if visit[nxt1][nxt2] is True:
                                    break
                                else:
                                    queue.append([nxt1, nxt2, is_sun, m + 1, day])
                                    break
                        else:
                            break

if arrived is True:
    if is_sun:
        print(day, 'sun')
    else:
        print(day, 'moon')
else:
    print(-1)
