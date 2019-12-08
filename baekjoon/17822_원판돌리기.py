from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')

N, M, T = map(int, input().split())
board = [collections.deque(list(map(int, input().split()))) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for t in range(T):
    x, d, k = map(int, input().split())     # x 배수 번호의 원판, d 방향으로, k 칸 회전

    for i in range(1, N // x + 1):
        xx = x * i - 1
        if d == 0:
            board[xx].rotate(k)
        else:
            board[xx].rotate(-k)

    flag = False
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                value = board[i][j]
                queue = collections.deque([(i, j)])
                while queue:
                    idx1, idx2 = queue.popleft()
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], (idx2 + adj[1]) % M
                        if 0 <= nxt1 < N:
                            if board[nxt1][nxt2] == value:
                                flag = True
                                queue.append((nxt1, nxt2))
                                board[nxt1][nxt2] = 0

    if flag is False:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] != 0:
                    total += board[i][j]
                    cnt += 1
        if cnt == 0:
            break
        else:
            avg = total / cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j] > avg:
                        board[i][j] -= 1
                    elif 0 < board[i][j] < avg:
                        board[i][j] += 1
# pprint(board)

result = 0
for i in range(N):
    result += sum(board[i])
print(result)
