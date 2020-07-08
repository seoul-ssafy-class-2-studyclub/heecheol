import sys
sys.stdin = open('input.txt', 'r')


def type_4():
    global max_sum

    for i in range(N):
        temp = sum(board[i][:4])
        if temp > max_sum:
            max_sum = temp
        for j in range(1, M-3):
            temp = temp - board[i][j-1] + board[i][j+3]
            if temp > max_sum:
                max_sum = temp

    for j in range(M):
        temp = board[0][j] + board[1][j] + board[2][j] + board[3][j]
        if temp > max_sum:
            max_sum = temp
        for i in range(1, N-3):
            temp = temp - board[i-1][j] + board[i+3][j]
            if temp > max_sum:
                max_sum = temp

    for i in range(N-1):
        for j in range(M-1):
            temp = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
            if temp > max_sum:
                max_sum = temp


def type_6():
    global max_sum

    for i in range(N-2):
        for j in range(M-1):
            temp1 = board[i][j] + board[i+1][j] + board[i+2][j]
            temp2 = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1]
            temp3 = board[i+1][j] + board[i+1][j+1]

            max_sum = max(max_sum, temp1 + board[i][j+1], temp1 + board[i+1][j+1], temp1 + board[i+2][j+1],
                          temp2 + board[i][j], temp2 + board[i+1][j], temp2 + board[i+2][j],
                          temp3 + board[i][j] + board[i+2][j+1], temp3 + board[i][j+1] + board[i+2][j])

    for i in range(N-1):
        for j in range(M-2):
            temp1 = board[i][j] + board[i][j+1] + board[i][j+2]
            temp2 = board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
            temp3 = board[i][j+1] + board[i+1][j+1]

            max_sum = max(max_sum, temp1 + board[i+1][j], temp1 + board[i+1][j+1], temp1 + board[i+1][j+2],
                          temp2 + board[i][j], temp2 + board[i][j+1], temp2 + board[i][j+2],
                          temp3 + board[i][j] + board[i+1][j+2], temp3 + board[i+1][j] + board[i][j+2])


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0
type_4()
type_6()
print(max_sum)
