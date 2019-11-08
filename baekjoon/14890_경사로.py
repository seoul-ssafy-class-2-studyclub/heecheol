import sys
sys.stdin = open('input.txt', 'r')

N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

for row in board:
    print(row)
    i = 0
    flag = True
    step = [False] * N

    while i < N - 1:
        if row[i] == row[i + 1]:
            i += 1
            continue

        elif abs(row[i] - row[i + 1]) > 1:
            flag = False
            break

        elif row[i] - row[i + 1] == 1:
            if i + L < N:
                arr = row[i + 1:i + L + 1]
                if len(set(arr)) == 1:
                    if i + L < N - 1 and row[i + L] - row[i + L + 1] == -1:
                        flag = False
                        break
                    else:
                        for j in range(i + 1, i + L + 1):
                            step[j] = True
                        i += L
                        continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break

        elif row[i] - row[i + 1] == -1:
            if i == 0 and L == 1:
                i += 1
                continue

            elif i - L >= 0:
                if len(set(row[i - L:i])) == 1 and len(set(step[i - L:i])) == 1 and step[i - L] is False:
                    i += 1
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break
    print(step)
    if flag is True:
        print(row, '*')
        cnt += 1

board = list(zip(*board))

for row in board:
    i = 0
    flag = True
    while i < N - 1:
        if row[i] == row[i + 1]:
            i += 1
            continue

        elif abs(row[i] - row[i + 1]) > 1:
            flag = False
            break

        elif row[i] - row[i + 1] == 1:
            if i + L < N:
                arr = row[i + 1:i + L + 1]
                if len(set(arr)) == 1:
                    i += L
                    if i < N - 1 and row[i] - row[i + 1] == -1:
                        flag = False
                        break
                    else:
                        continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break

        elif row[i] - row[i + 1] == -1:
            if i == 0 and L == 1:
                i += 1
                continue

            elif i - L >= 0:
                arr = row[i - L:i]
                if len(set(arr)) == 1:
                    i += 1
                    continue
                else:
                    flag = False
                    break
            else:
                flag = False
                break

    if flag is True:
        # print(row)
        cnt += 1

print(cnt)


