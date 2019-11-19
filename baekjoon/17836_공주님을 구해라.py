import collections
import sys
sys.stdin = open('input.txt', 'r')


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]

queue = collections.deque([(0, 0)])
result = float('inf')
flag1 = False
flag2 = False
time = 0

while queue:
    if time > T:
        break

    for _ in range(len(queue)):
        idx1, idx2 = queue.popleft()
        if idx1 == N - 1 and idx2 == M - 1:
            result = time
            flag2 = True
            break

        elif board[idx1][idx2] == 0:
            board[idx1][idx2] = 1
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board[nxt1][nxt2] != 1:
                        queue.append((nxt1, nxt2))

        elif flag1 is False and board[idx1][idx2] == 2:
            if time + abs(idx1 - N + 1) + abs(idx2 - M + 1) <= T:
                T = time + abs(idx1 - N + 1) + abs(idx2 - M + 1)
                flag1 = True

    if flag2 is True:
        break
    else:
        time += 1

if flag2 is True:
    print(result)
elif flag1 is True:
    print(T)
else:
    print('Fail')




