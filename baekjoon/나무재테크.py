from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def spring1(idx1, idx2, arr):
    age_tree = arr[0]
    if board[idx1][idx2] >= age_tree:
        board[idx1][idx2] -= age_tree
        arr[0] += 1
    else:
        board[idx1][idx2] += age_tree // 2
        arr.pop()


def spring2(idx1, idx2, arr):
    t = 0
    while t < len(arr):
        if board[idx1][idx2] >= arr[t]:
            board[idx1][idx2] -= arr[t]
            arr[t] += 1
            t += 1
        else:
            for n in range(len(arr) - 1, t - 1, -1):
                board[idx1][idx2] += arr.pop() // 2
            break


def fall(idx1, idx2):
    adj_list = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for adj in adj_list:
        nxt1 = idx1 + adj[0]
        nxt2 = idx2 + adj[1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            trees[nxt1][nxt2].append(1)


N, M, K = map(int, input().split())

board = [[5] * N for _ in range(N)]
water = [list(map(int, input().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(M):
    row, col, age = map(int, input().split())
    trees[row - 1][col - 1].append(age)

for k in range(K):
    for i in range(N):
        for j in range(N):
            if trees[i][j]:
                if len(trees[i][j]) > 1:
                    trees[i][j].sort()
                    spring2(i, j, trees[i][j])
                else:
                    spring1(i, j, trees[i][j])

    for i in range(N):
        for j in range(N):
            board[i][j] += water[i][j]
            if trees[i][j]:
                for tr in range(len(trees[i][j]) - 1, -1, -1):
                    if trees[i][j][tr] % 5 == 0:
                        fall(i, j)

cnt = 0
for i in range(N):
    for j in range(N):
        if trees[i][j]:
            cnt += len(trees[i][j])

print(cnt)
