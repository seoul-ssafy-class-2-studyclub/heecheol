import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0

for row in board:
    flat = 1
    j = 0
    flag = True
    while j < N - 1:
        if row[j] == row[j + 1]:
            flat += 1
            j += 1
            continue
        elif abs(row[j] - row[j + 1]) > 1:
            flag = False
            break
        elif row[j] - row[j + 1] == 1:
            if j + L < N:
                for nj in range(j + 1, j + L):
                    if row[nj] == row[nj + 1]:
                        continue
                    else:
                        flag = False
                        break
                if flag is True:
                    flat = 0
                    j += L
                    continue
                else:
                    break
            else:
                flag = False
                break
        else:
            if flat >= L:
                flat = 1
                j += 1
                continue
            else:
                flag = False
                break

    if flag is True:
        cnt += 1

board2 = list(map(list, zip(*board)))
for row in board2:
    flat = 1
    j = 0
    flag = True
    while j < N - 1:
        if row[j] == row[j + 1]:
            flat += 1
            j += 1
            continue
        elif abs(row[j] - row[j + 1]) > 1:
            flag = False
            break
        elif row[j] - row[j + 1] == 1:
            if j + L < N:
                for nj in range(j + 1, j + L):
                    if row[nj] == row[nj + 1]:
                        continue
                    else:
                        flag = False
                        break
                if flag is True:
                    flat = 0
                    j += L
                    continue
                else:
                    break
            else:
                flag = False
                break
        else:
            if flat >= L:
                flat = 1
                j += 1
                continue
            else:
                flag = False
                break

    if flag is True:
        cnt += 1

print(cnt)
