from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def paint_and_calculate(x, y, d1, d2):
    board = [[5] * N for _ in range(N)]
    people = [0] * 6

    edge = [(x, y)]
    for d in range(1, d1):
        edge.append((x+d, y-d))

    for i in range(x+d1):
        for j in range(y+1):
            if (i, j) not in edge:
                board[i][j] = 1
            else:
                break

    edge = []
    for d in range(1, d2+1):
        edge.append((x+d, y+d))

    for i in range(x+d2+1):
        for j in range(N-1, y, -1):
            if (i, j) not in edge:
                board[i][j] = 2
            else:
                break

    edge = [(x+d1, y-d1)]
    for d in range(1, d2+1):
        edge.append((x+d1+d, y-d1+d))

    for i in range(x+d1, N):
        for j in range(y-d1+d2):
            if (i, j) not in edge:
                board[i][j] = 3
            else:
                break

    edge = [(x+d2, y+d2)]
    for d in range(1, d1+1):
        edge.append((x+d2+d, y+d2-d))

    for i in range(x+d2+1, N):
        for j in range(N-1, y-d1+d2-1, -1):
            if (i, j) not in edge:
                board[i][j] = 4
            else:
                break

    for i in range(N):
        for j in range(N):
            people[board[i][j]] += population[i][j]

    return max(people) - min(people[1:])


N = int(input())
population = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')
for X in range(0, N-2):
    for Y in range(1, N-1):
        for D1 in range(1, min(Y+1, N-X-1)):
            for D2 in range(1, min(N-Y, N-X-D1)):
                diff = paint_and_calculate(X, Y, D1, D2)
                if diff < result:
                    result = diff

print(result)
