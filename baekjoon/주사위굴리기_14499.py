import sys
sys.stdin = open('input.txt', 'r')


def east():
    dice[0], dice[2], dice[3], dice[5] = [dice[3], dice[0], dice[5], dice[2]]


def west():
    dice[0], dice[2], dice[3], dice[5] = [dice[2], dice[5], dice[0], dice[3]]


def north():
    dice[0], dice[1], dice[4], dice[5] = [dice[4], dice[0], dice[5], dice[1]]


def south():
    dice[0], dice[1], dice[4], dice[5] = [dice[1], dice[5], dice[0], dice[4]]


def check_bottom(i, j):
    if board[i][j] == 0:
        board[i][j] = dice[5]
    else:
        dice[5], board[i][j] = board[i][j], 0


N, M, x, y, K = map(int, input().split())

board = [list(input().split()) for _ in range(N)]
dice = ['0'] * 6

answer = []

for d in input().split():
    if d == '1':
        if y < M - 1:
            y += 1
            east()
            check_bottom(x, y)
            answer.append(dice[0])
            # print(dice[0])

    elif d == '2':
        if y > 0:
            y -= 1
            west()
            check_bottom(x, y)
            answer.append(dice[0])
            # print(dice[0])

    elif d == '3':
        if x > 0:
            x -= 1
            north()
            check_bottom(x, y)
            answer.append(dice[0])
            # print(dice[0])

    else:
        if x < N - 1:
            x += 1
            south()
            check_bottom(x, y)
            answer.append(dice[0])
            # print(dice[0])

print('\n'.join(answer))
