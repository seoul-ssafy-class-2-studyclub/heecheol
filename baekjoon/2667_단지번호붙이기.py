import sys
sys.stdin = open('input.txt', 'r')


def bfs(idx1, idx2):
    global cnt
    cnt += 1
    board[idx1][idx2] = '0'

    for adj in adj_list:
        nxt1 = idx1 + adj[0]
        nxt2 = idx2 + adj[1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N and board[nxt1][nxt2] == '1':
            bfs(nxt1, nxt2)


N = int(input())
board = [list(input()) for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
result = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            cnt = 0
            bfs(i, j)
            result.append(cnt)

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])

