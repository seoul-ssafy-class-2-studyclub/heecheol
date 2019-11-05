import sys
sys.stdin = open('input.txt', 'r')


# numbering
def numbering(ix, iy, num):
    board[ix][iy] = num

    for adj in adj_list:
        nxt1 = ix + adj[0]
        nxt2 = iy + adj[1]
        if board[nxt1][nxt2] == '#':
            numbering(nxt1, nxt2, num)


# 인접리스트 만들기
# arr = [시작값]
# '.' 으로 이동하면서 '.'이 아니고 arr에 없는 값이다 -> arr.append
# 양방향 그래프
def is_connect(idx1, idx2, s):
    value = board[idx1][idx2]
    # print(s, ',', idx1, idx2, value)

    if value not in linked[s]:
        # print('#')
        linked[s].append(value)
        linked[value].append(s)

    else:
        if value == '.' and visit[idx1][idx2] is False:
            visit[idx1][idx2] = True
            for adj in adj_list:
                nxt1 = idx1 + adj[0]
                nxt2 = idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    # visit[nxt1][nxt2] = True
                    is_connect(nxt1, nxt2, s)
                    # visit[nxt1][nxt2] = False
            visit[idx1][idx2] = False


# #########################
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(N):
    board[i][0] = 0
    board[i][M - 1] = 0
for j in range(M):
    board[0][j] = 0
    board[N - 1][j] = 0

n = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == '#':
            n += 1
            numbering(i, j, n)

linked = [['.'] for _ in range(n + 1)]

ni = 1
flag1 = True
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == ni:
            linked[ni].append(ni)
            for adj in adj_list:
                nxt1 = i + adj[0]
                nxt2 = j + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if board[nxt1][nxt2] == '.' or board[nxt1][nxt2] == 0:
                        visit = [[False] * M for _ in range(N)]
                        visit[i][j] = True
                        is_connect(nxt1, nxt2, ni)
            ni += 1
            if ni > n:
                flag1 = False
                break
    if flag1 is False:
        break

print(linked)

for i in range(n + 1):
    linked[i].pop(0)

print(linked)