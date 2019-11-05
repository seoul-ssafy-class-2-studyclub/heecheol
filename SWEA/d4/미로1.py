import sys
sys.stdin = open('input.txt', 'r')

N = 16
for t in range(10):
    tc = int(input())
    board = [list(input()) for n in range(N)]

    flag = True
    for i in range(N):
        for j in range(N):
            if board[i][j] == '2':
                si = i
                sj = j
                flag = False
                break
        if flag == False:
            break

    stack = [(si, sj)]
    near = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    flag = True
    result = 0
    while stack:
        i, j = stack.pop()
        board[i][j] = '1'

        for ne in near:
            ni = i+ne[0]
            nj = j+ne[1]
            if 0 <= ni < N and 0 <= nj < N:
                if board[ni][nj] == '0':
                    stack.append((ni, nj))
                elif board[ni][nj] == '3':
                    flag = False
                    break
        
        if flag == False:
            result = 1
            break

    print(f'#{tc} {result}')

