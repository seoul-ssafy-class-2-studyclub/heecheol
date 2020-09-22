import sys
sys.stdin = open('input.txt', 'r')


H, W = map(int, input().split())
heights = list(map(int, input().split()))

board = [[0] * W for _ in range(H)]

for j in range(W):
    height = heights[j]
    for i in range(height):
        board[H-i-1][j] = 1

answer = 0
for i in range(H):
    blocked = False
    cnt = 0
    for j in range(W):
        if board[i][j] == 1:
            if blocked:
                answer += cnt
                cnt = 0
            else:
                blocked = True
        else:
            if blocked:
                cnt += 1
            else:
                continue

print(answer)
