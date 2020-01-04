import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
targets = []
si = sj = -1
for i in range(N):
    for j in range(M):
        if board[i][j] == '.' or board[i][j] == '#':
            continue
        if board[i][j] == 'S':
            si, sj = i, j
        else:
            targets.append((i, j))

# 이동횟수, 배달횟수, 배달위치, 오, 아, 왼, 위
dp = [[(-1, -1, 4, 0, 0)] * M for _ in range(N)]
# n_dir => 직전 방향이 오, 아, 왼, 위, 시작 순
n_dir = [[()]]
queue = [(0, si, sj)]

while queue:
    n, idx1, idx2 = queue.pop(0)
