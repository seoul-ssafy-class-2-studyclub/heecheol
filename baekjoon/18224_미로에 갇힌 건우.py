# from pprint import pprint
import collections
import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = collections.deque([(0, 0)])
is_moon = 0
cnt = 1

flag = False
visit = [[[-1] * M for _ in range(N)] for _ in range(N)]

while queue:

    for _ in range(len(queue)):
        idx1, idx2 = queue.popleft()
        if idx1 == idx2 == N - 1:
            flag = True
            break

        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < N:
                if board[nxt1][nxt2] == 0:
                    if visit[nxt1][nxt2][cnt % M] == is_moon or visit[nxt1][nxt2][cnt % M] == 2:
                        continue
                    if is_moon == 0:
                        visit[nxt1][nxt2][cnt % M] += 1
                    else:
                        visit[nxt1][nxt2][cnt % M] += 2
                    queue.append((nxt1, nxt2))
                else:
                    if is_moon == 1:
                        while True:
                            nxt1 += adj[0]
                            nxt2 += adj[1]
                            if 0 <= nxt1 < N and 0 <= nxt2 < N:
                                if board[nxt1][nxt2] == 1:
                                    continue
                                else:
                                    if visit[nxt1][nxt2][cnt % M] == is_moon or visit[nxt1][nxt2][cnt % M] == 2:
                                        break
                                    visit[nxt1][nxt2][cnt % M] += 2
                                    queue.append((nxt1, nxt2))
                                    break
                            else:
                                break
    # pprint(visit)

    if flag is True:
        break
    if cnt % M == 0:
        is_moon = -(is_moon - 1)
    cnt += 1
# print(cnt)

if flag is True:
    if is_moon == 0:
        answer = 'sun'
    else:
        answer = 'moon'
    day = (cnt - 1) // (2 * M) + 1
    print(day, answer)
else:
    print(-1)
