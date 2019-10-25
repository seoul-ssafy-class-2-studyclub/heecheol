from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
population = [list(map(int, input().split())) for _ in range(N)]
min_diff = 987654321
finish = False

for idx1 in range(N - 2):
    for idx2 in range(1, N - 1):

        for right in range(1, N - idx2):
            for left in range(1, idx2 + 1):
                if idx1 + right + left < N:
                    board = [[4] * N for _ in range(N)]
                    people = [0] * 5

                    # board <= 1, 2, 3, 4
                    for i in range(idx1 + left):
                        for j in range(idx2 + 1):
                            board[i][j] = 0
                    for i in range(idx1 + right + 1):
                        for j in range(idx2 + 1, N):
                            board[i][j] = 1
                    for i in range(idx1 + left, N):
                        for j in range(idx2 + right - left):
                            board[i][j] = 2
                    for i in range(idx1 + right + 1, N):
                        for j in range(idx2 + right - left, N):
                            board[i][j] = 3

                    # board <= 5
                    for d1 in range(left):
                        for d2 in range(d1 + 1):
                            board[idx1 + d1][idx2 - d2] = 4
                    for d1 in range(right):
                        for d2 in range(d1 + 1):
                            board[idx1 + d1 + 1][idx2 + d2 + 1] = 4
                    for d1 in range(right):
                        for d2 in range(d1 + 1):
                            board[idx1 + left + right - 1 - d1][idx2 + right - left - 1 - d2] = 4
                    for d1 in range(left):
                        for d2 in range(d1 + 1):
                            board[idx1 + left + right - d1][idx2 + right - left + d2] = 4

                    # sum each part
                    for i in range(N):
                        for j in range(N):
                            people[board[i][j]] += population[i][j]

                    result = max(people) - min(people)
                    if result < min_diff:
                        min_diff = result
                        if result == 0:
                            finish = True
                            break
            if finish is True:
                break
        if finish is True:
            break
    if finish is True:
        break
print(min_diff)

