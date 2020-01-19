import sys
input = sys.stdin.readline


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

before_jump = [[0] * M for _ in range(N)]
before_jump[0][0] = board[0][0]
for i in range(1, M):
    before_jump[0][i] = before_jump[0][i - 1] + board[0][i]

for row in range(1, N):
    after_jump = [0] * M
    for i in range(M):
        after_jump[i] = before_jump[row - 1][i] + board[row][i]
    # print(after_jump)

    right = [0] * M
    right[0] = after_jump[0]
    for i in range(1, M):
        right[i] = max(after_jump[i], right[i - 1] + board[row][i])

    left = [0] * M
    left[-1] = after_jump[-1]
    for i in range(M - 2, -1, -1):
        left[i] = max(after_jump[i], left[i + 1] + board[row][i])

    for i in range(M):
        before_jump[row][i] = max(right[i], left[i])

# pprint(before_jump)
print(before_jump[-1][-1])
