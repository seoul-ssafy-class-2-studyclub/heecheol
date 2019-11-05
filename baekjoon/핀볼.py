import sys
sys.stdin = open('input.txt', 'r')


def move(i, j, d):
    cnt = 0
    while board[i][j] != -1:
        if 1 <= board[i][j] <= 5:
            cnt += 1

            # 1번 삼각형
            if board[i][j] == 1:
                if d == 'U':
                    d = 'D'
                    i += 1
                    while board[i][j] == 0:
                        i += 1
                    continue
                elif d == 'R':
                    d = 'L'
                    j -= 1
                    while board[i][j] == 0:
                        j -= 1
                    continue

                elif d == 'D':
                    d = 'R'
                    j += 1
                    if j == N:
                        cnt += 1
                        j -= 1
                        d = 'L'
                    else:
                        while board[i][j] == 0:
                            if d == 'R':
                                j += 1
                            # elif d == 'L':
                            else:
                                j -= 1
                            if j == N:
                                cnt += 1
                                j -= 1
                                d = 'L'
                    continue
                else:
                    d = 'U'
                    i -= 1
                    if i == -1:
                        cnt += 1
                        i += 1
                        d = 'D'
                    else:
                        while board[i][j] == 0:
                            if d == 'U':
                                i -= 1
                            # elif d == 'D':
                            else:
                                i += 1
                            if i == -1:
                                cnt += 1
                                i += 1
                                d = 'D'
                    continue


            # 2번 삼각형
            elif board[i][j] == 2:
                # up
                if d == 'U':
                    d = 'R'
                    j += 1
                    if j == N:
                        cnt += 1
                        j -= 1
                        d = 'L'
                    else:
                        while board[i][j] == 0:
                            if d == 'R':
                                j += 1
                            # elif d == 'L':
                            else:
                                j -= 1
                            if j == N:
                                cnt += 1
                                j -= 1
                                d = 'L'
                    continue
                # left
                elif d == 'L':
                    d = 'D'
                    i += 1
                    if i == N:
                        cnt += 1
                        i -= 1
                        d = 'U'
                    else:
                        while board[i][j] == 0:
                            if d == 'D':
                                i += 1
                            else:
                                i -= 1
                            if i == N:
                                cnt += 1
                                i -= 1
                                d = 'U'
                    continue

                # down
                elif d == 'D':
                    d = 'U'
                    i += 1
                    while board[i][j] == 0:
                        i += 1
                    continue

                # right
                else:
                    d = 'L'
                    j -= 1
                    while board[i][j] == 0:
                        j -= 1

            # 3번 삼각형
            elif board[i][j] == 3:
                # up
                if d == 'U':
                    d = 'L'
                    j -= 1
                    if j == -1:
                        cnt += 1
                        j += 1
                        d = 'R'
                    else:
                        while board[i][j] == 0:
                            if d == 'L':
                                j -= 1
                            else:
                                j += 1
                            if j == -1:
                                cnt += 1
                                j += 1
                                d = 'R'
                    continue
                # right
                elif d == 'R':
                    d = 'D'
                    i += 1
                    if i == N:
                        cnt += 1
                        i -= 1
                        d = 'U'
                    else:
                        while board[i][j] == 0:
                            if d == 'D':
                                i += 1
                            else:
                                i -= 1
                            if i == N:
                                cnt += 1
                                i -= 1
                                d = 'U'
                    continue
                # down
                elif d == 'D':
                    d = 'U'
                    i += 1
                    while board[i][j] == 0:
                        i += 1
                    continue
                # left
                else:
                    d = 'R'
                    j += 1
                    while board[i][j] == 0:
                        j += 1

            # 4번 삼각형
            elif board[i][j] == 4:
                if d == 'U':
                    d = 'D'
                    i += 1
                    while board[i][j] == 0:
                        i += 1
                    continue

                elif d == 'L':
                    d = 'R'
                    j += 1
                    while board[i][j] == 0:
                        j += 1
                    continue

                elif d == 'D':
                    d = 'L'
                    j -= 1
                    if j == -1:
                        cnt += 1
                        j += 1
                        d = 'R'
                    else:
                        while board[i][j] == 0:
                            if d == 'R':
                                j += 1
                            # elif d == 'L':
                            else:
                                j -= 1
                            if j == -1:
                                cnt += 1
                                j += 1
                                d = 'R'
                    continue
                else:
                    d = 'U'
                    i -= 1
                    if i == -1:
                        cnt += 1
                        i += 1
                        d = 'D'
                    else:
                        while board[i][j] == 0:
                            if d == 'U':
                                i -= 1
                            # elif d == 'D':
                            else:
                                i += 1
                            if i == -1:
                                cnt += 1
                                i += 1
                                d = 'D'
                    continue


# ##########################################



for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    dirs = ['U', 'D', 'R', 'L']

    for ii in range(N):
        for jj in range(N):
            if board[ii][jj] == 0:
                board[ii][jj] = -1
                for dd in dirs:
                    if dd == 'U':
                        move(ii - 1, jj, dd)
                    elif dd == 'D':
                        move(ii + 1, jj, dd)
                    elif dd == 'R':
                        move(ii, jj + 1, dd)
                    else:
                        move(ii, jj - 1, dd)
                board[ii][jj] = 0