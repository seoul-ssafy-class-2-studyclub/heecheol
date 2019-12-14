import sys
sys.stdin = open('input.txt', 'r')

N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
roll = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

for i in range(K):
    r = roll[i]
    if r == 1:
        if y + 1 < M:
            y += 1
            dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
        else:
            continue
    elif r == 2:
        if y - 1 >= 0:
            y -= 1
            dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
        else:
            continue
    elif r == 3:
        if x - 1 >= 0:
            x -= 1
            dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
        else:
            continue
    elif r == 4:
        if x + 1 < N:
            x += 1
            dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]
        else:
            continue

    if board[x][y] == 0:
        board[x][y] = dice[6]
    else:
        dice[6] = board[x][y]
        board[x][y] = 0

    print(dice[1])
