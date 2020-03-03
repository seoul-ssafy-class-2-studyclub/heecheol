import collections


T = int(input())
adj_list = [(0, -1), (-1, -1), (-1, 0), (0, 1), (1, 1), (1, 0)]

for tc in range(T):
    a, b = map(int, input().split())

    if a > b:
        big = a
        small = b
    elif a < b:
        big = b
        small = a
    else:
        print('#{} 0'.format(tc))
        continue

    # create list
    n = temp = 1
    while temp < big:
        n += 1
        temp += n

    num_list = [[0] * n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(i + 1):
            num_list[i][j] = num
            num += 1

    visit = [[False] * n for _ in range(n)]

    queue = collections.deque([(n - 1, num_list[-1].index(big))])
    visit[n - 1][num_list[-1].index(big)] = True

    time = 0
    flag = True
    while flag:
        time += 1
        for _ in range(len(queue)):
            idx1, idx2 = queue.popleft()

            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]

                if 0 <= nxt1 < n and 0 <= nxt2 <= nxt1:
                    if visit[nxt1][nxt2] is False:
                        if num_list[nxt1][nxt2] == small:
                            flag = False
                            break
                        visit[nxt1][nxt2] = True
                        queue.append((nxt1, nxt2))

            if flag is False:
                break

    print('#{} {}'.format(tc, time))
