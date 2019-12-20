import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

queue = [(0, 0, 1)]
while queue:
    idx1, idx2, n = queue.pop(0)
    if board[idx1][idx2] == '1':
        if idx1 == N - 1 and idx2 == M - 1:
            break

        board[idx1][idx2] = '0'

        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                if board[nxt1][nxt2] == '1':
                    queue.append((nxt1, nxt2, n + 1))

print(n)