from pprint import pprint
import heapq
import sys
sys.stdin = open('input.txt', 'r')


tc = 0
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

while True:
    tc += 1
    N = int(input())

    if N == 0:
        break

    else:
        board = [list(map(int, input().split())) for _ in range(N)]

        visit = [[False] * N for _ in range(N)]

        queue = []
        heapq.heappush(queue, (board[0][0], 0, 0))

        while queue:
            money, idx1, idx2 = heapq.heappop(queue)

            if idx1 == N - 1 and idx2 == N - 1:
                break

            if visit[idx1][idx2] is False:
                visit[idx1][idx2] = True

                for adj in adj_list:
                    nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < N and visit[nxt1][nxt2] is False:
                        heapq.heappush(queue, (money + board[nxt1][nxt2], nxt1, nxt2))

        print('Problem {}: {}'.format(tc, money))
        