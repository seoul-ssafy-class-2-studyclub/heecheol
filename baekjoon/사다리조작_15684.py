import sys
sys.stdin = open('input.txt', 'r')
import itertools


def is_correct():
    for num in range(N-1):
        r, c = 1, num
        while r <= H:
            if ladder[r][c] == 'D':
                r += 1
            elif ladder[r][c] == 'L':
                r += 1
                c -= 1
            else:
                r += 1
                c += 1

        if c == num:
            continue
        else:
            return False
    return True


def if_add_one():
    for i, j in possible:
        ladder[i][j] = 'R'
        ladder[i][j+1] = 'L'
        if is_correct():
            return True
        else:
            ladder[i][j] = ladder[i][j+1] = 'D'
    return False


def if_add_two():
    if len(possible) < 2:
        return False
    else:
        for new_ladders in list(itertools.combinations(possible, 2)):
            for new in new_ladders:
                if (new[0], new[1] + 1) in new_ladders:
                    break
            else:
                for i, j in new_ladders:
                    ladder[i][j] = 'R'
                    ladder[i][j + 1] = 'L'
                if is_correct():
                    return True
                else:
                    for i, j in new_ladders:
                        ladder[i][j] = ladder[i][j + 1] = 'D'
    return False


def if_add_three():
    if len(possible) < 3:
        return False
    else:
        for new_ladders in list(itertools.combinations(possible, 3)):
            for new in new_ladders:
                if (new[0], new[1] + 1) in new_ladders:
                    break
            else:
                for i, j in new_ladders:
                    ladder[i][j] = 'R'
                    ladder[i][j + 1] = 'L'
                if is_correct():
                    return True
                else:
                    for i, j in new_ladders:
                        ladder[i][j] = ladder[i][j + 1] = 'D'
    return False


N, M, H = map(int, input().split())
ladder = [['D'] * N for _ in range(H + 2)]

for _ in range(M):
    row, col = map(int, input().split())
    ladder[row][col-1] = 'R'
    ladder[row][col] = 'L'

possible = []
for row in range(1, H + 1):
    for col in range(N - 1):
        if ladder[row][col] == 'D' and ladder[row][col+1] == 'D':
            possible.append((row, col))

if is_correct():
    print(0)
else:
    if if_add_one():
        print(1)
    elif if_add_two():
        print(2)
    elif if_add_three():
        print(3)
    else:
        print(-1)
