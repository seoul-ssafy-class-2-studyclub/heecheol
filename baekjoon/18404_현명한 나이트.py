import collections
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
X, Y = map(int, input().split())
board = [[0] * N for _ in range(N)]

for m in range(1, M + 1):
    A, B = map(int, input().split())
    board[A - 1][B - 1] = m

adj_list = [(-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]
queue = collections.deque([(X - 1, Y - 1, 1)])

board[X - 1][Y - 1] = -1

find = 0
answer = [0] * M
flag = False
while queue:
    idx1, idx2, cnt = queue.popleft()

    for adj in adj_list:
        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if board[nxt1][nxt2] == -1:
                continue
            elif board[nxt1][nxt2] == 0:
                board[nxt1][nxt2] = -1
                queue.append((nxt1, nxt2, cnt + 1))
                continue
            else:
                answer[board[nxt1][nxt2] - 1] = str(cnt)
                find += 1
                if find == M:
                    flag = True
                    break
                board[nxt1][nxt2] = -1
                queue.append((nxt1, nxt2, cnt + 1))
                continue
    if flag is True:
        break

print(' '.join(answer))
