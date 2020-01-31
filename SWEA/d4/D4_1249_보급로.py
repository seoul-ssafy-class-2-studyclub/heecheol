import sys
sys.stdin = open('input.txt', 'r')
import heapq


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, list(input()))) for _ in range(N)]

    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    inf = float('inf')
    dp = [[inf] * N for _ in range(N)]

    queue = []
    heapq.heappush(queue, [0, 0, 0])
    while queue:
        time, idx1, idx2 = heapq.heappop(queue)
        if idx1 == idx2 == N - 1:
            break

        if time < dp[idx1][idx2]:
            dp[idx1][idx2] = time
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if dp[nxt1][nxt2] == inf:
                        heapq.heappush(queue, [time + board[nxt1][nxt2], nxt1, nxt2])
    print('#{} {}'.format(tc, time))
