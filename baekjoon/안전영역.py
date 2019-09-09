# 안전 영역 (백준)

import sys
sys.stdin = open('2468.txt', 'r')


def island(ix, iy):
    stack = [(ix, iy)]
    near = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    while stack:
        i, j = stack.pop()
        visit[i][j] = True
        for ne in near:
            ni = i+ne[0]
            nj = j+ne[1]
            if 0 <= ni < N and 0 <= nj < N:
                if visit[ni][nj] is False and sank[ni][nj] is False:
                    stack.append((ni, nj))


N = int(input())
board = [list(map(int, input().split())) for n in range(N)]

sank = [[False]*N for n in range(N)]

cnt_list = []
for level in range(100):
    for i in range(N):
        for j in range(N):
            if sank[i][j] is False and board[i][j] - level == 0:
                sank[i][j] = True

    cnt = 0
    visit = [[False]*N for n in range(N)]

    for i in range(N):
        for j in range(N):
            if visit[i][j] is False and sank[i][j] is False:
                island(i, j)
                cnt += 1
    if cnt == 0:
        break

    cnt_list.append(cnt)

print(max(cnt_list))