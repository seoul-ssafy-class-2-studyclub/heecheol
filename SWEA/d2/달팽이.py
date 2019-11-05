N = int(input())

board = [[0 for n in range(N)] for n in range(N)]

di = 0
number = 0
i = 0, j = 0
for n in range(N**2):
    board[i][j] = number
    number += 1

    if di % 4 == 0:     # 방향, di 언제 바꾸지
        j += 1
        
    elif di % 4 == 1:
        i += 1

    elif di % 4 == 2:
        j -= 1

    else:
        i -= 1

    count += 1