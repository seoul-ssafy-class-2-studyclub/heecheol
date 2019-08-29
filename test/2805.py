# 농작물 수확하기
import sys
sys.stdin = open('2805.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(input()) for n in range(N)]

    cen = N // 2
    money = 0
    for row in range(0, cen+1):
        for col in range(cen-row, cen+row+1):
            money += int(board[row][col])
    for row in range(cen+1, N):
        for col in range(row-cen, N-row+cen):
            money += int(board[row][col])

    print('#{} {}'.format(tc, money))
