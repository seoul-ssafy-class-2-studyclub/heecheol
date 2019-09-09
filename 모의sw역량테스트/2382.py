from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


TC = int(input())
for tc in range(1, TC+1):
    N, M, K = map(int, input().split())
    board = [0]*K

    for k in range(K):
        # row, col, num, di 
        board[k] = list(map(int, input().split()))

    for i in range(1, 2*N):
        if i > M:
            M = 0
            break
        for data in board:
            if data != False:
                if data[3] == 1:
                    data[0] -= 1
                    if data[0] == 0:
                        data[2] //= 2
                        data[3] = 2
                elif data[3] == 2:
                    data[0] += 1
                    if data[0] == N-1:
                        data[2] //= 2
                        data[3] = 1                    
                elif data[3] == 3:
                    data[1] -= 1
                    if data[1] == 0:
                        data[2] //= 2
                        data[3] = 4
                elif data[3] == 4:
                    data[1] += 1
                    if data[1] == N-1:
                        data[2] //= 2
                        data[3] = 3
        print(board)

        # check # 작은부분 0, 0, 0, 0 으로
        for i in range(K):
            for j in range(i+1, K):
                if board[i] != False and board[j] != False:
                    if board[i][0] == board[j][0] and board[i][1] == board[j][1]:
                        if board[i][2] > board[j][2]:
                            board[i][2] += board[j][2]
                            board[j] = False
                        else:
                            board[j][2] += board[i][2]
                            board[i] = False
                else:
                    break

    if M != 0:
        M -= (2*N - 2)
            
        for i in range(K):
            if board[i] != False:
                for half in range(M//(N-1)):    # 두배로 하면 줄일 수 있을듯
                    board[i][2] //= 2
                    if board[i][2] == 0:
                        break

        M %= (N-1)

        for i in range(M):
            for data in board:
                if data != False:
                    if data[3] == 1:
                        data[0] -= 1
                        if data[0] == 0:
                            data[2] //= 2
                            data[3] = 2
                    elif data[3] == 2:
                        data[0] += 1
                        if data[0] == N-1:
                            data[2] //= 2
                            data[3] = 1                    
                    elif data[3] == 3:
                        data[1] -= 1
                        if data[1] == 0:
                            data[2] //= 2
                            data[3] = 4
                    elif data[3] == 4:
                        data[1] += 1
                        if data[1] == N-1:
                            data[2] //= 2
                            data[3] = 3

    total = 0
    for i in range(K):
        if board[i] != False:
            total += board[i][2]
    print(total)