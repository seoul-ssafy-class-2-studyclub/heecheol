from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')

K = int(input())
W, H = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(H)]
dp = [[[] for _ in range(W)] for _ in range(H)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
jump_list = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)]

queue = collections.deque([(0, 0, 0, K)])  # (row, col, 지금까지 움직임 수, 남은 horse 점프)
flag = False  # 도착해서 끝났는지 아니면 더이상 갈 곳이 없어서 끝났는지 구분하기 위한 flag
nn = 0
while queue:
    idx1, idx2, n, j = queue.popleft()

    if n == nn:
        pprint(dp)
        nn += 1

    if idx1 == H - 1 and idx2 == W - 1:  # 도착점이면 flag = True, break
        flag = True
        break

    else:
        for adj in adj_list:  # 인접한 네 방향으로의 움직임
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < H and 0 <= nxt2 < W:
                if board[nxt1][nxt2] == 0:  # 장애물이 없고
                    if j not in dp[nxt1][nxt2]:  # 다음 갈 곳 dp에 같은 점프 수로 이미 왔었니?
                        dp[nxt1][nxt2].append(j)  # 아니라면 dp에 남은 점프 수를 넣고
                        queue.append((nxt1, nxt2, n + 1, j))  # queue에도 넣어줘

                    # 같은 점프 수로 같은 칸에 왔어도 그때의 움직임 수(n)보다 지금 움직임 수가
                    # 무조건 작거나 같으므로 (queue니까) 무시해도 됩니다.

        if j > 0:  # 만약에 남은 점프 수가 0이 아니라면
            for jump in jump_list:  # 점프할 수 있는 8방향에 대해서
                nxt1, nxt2 = idx1 + jump[0], idx2 + jump[1]
                if 0 <= nxt1 < H and 0 <= nxt2 < W:
                    if board[nxt1][nxt2] == 0:
                        if j - 1 not in dp[nxt1][nxt2]:
                            # 다음 갈 곳에 같은 점프 수(j - 1)로 왔었니?
                            # 이때 점프를 해서 도착하는 거니까 남은 점프 수 => j - 1
                            dp[nxt1][nxt2].append(j - 1)  # 없으면 dp랑 queue에 넣어줘
                            queue.append((nxt1, nxt2, n + 1, j - 1))

if flag is True:
    print(n)
else:
    print(-1)