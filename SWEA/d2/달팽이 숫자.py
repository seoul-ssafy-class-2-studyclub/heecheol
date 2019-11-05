from pprint import pprint

N = int(input())

matrix = [[0 for col in range(N)] for row in range(N)]
j = 0
num = 1

for j in range(2):
    for i in range(N - j - 1):
        matrix[j][i] = num
        num += 1
        pprint(matrix)
    for i in range(N - j - 1):
        matrix[i][N-j-1] = num
        num += 1
        pprint(matrix)
        print(i, j)
    for i in range(N - j - 1):
        matrix[4-j][4-i] = num
        num += 1
        pprint(matrix)
    for i in range(N - j - 1):
        matrix[4-i][4-N+j+1] = num
        num += 1
        pprint(matrix)