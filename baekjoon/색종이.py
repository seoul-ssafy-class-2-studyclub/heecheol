import sys
sys.stdin = open('input.txt', 'r')

board = [[0]*101 for i in range(101)]

N = int(input())
for n in range(1, N+1):
    x, y, lx, ly = map(int, input().split())

    for i in range(x, x+lx):
        for j in range(y, y+ly):
            board[i][j] = n

for n in range(1, N+1):
    cnt = 0    
    for i in range(101):
        for j in range(101):
            if board[i][j] == n:
                cnt += 1
    print(cnt)

