# import sys
# sys.stdin = open('input.txt', 'r')
import collections

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
# print(board)

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j].isalpha():
            if board[i][j] == 'B':
                board[i][j] = '.'
                sbi, sbj = i, j
            elif board[i][j] == 'R':
                board[i][j] = '.'
                sri, srj = i, j

queue = collections.deque([(sbi, sbj, sri, srj, 4)])
next_dirs = {
    0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0, 1, 2, 3]
}

cnt = 1
flag = False
while cnt <= 10:
    for _ in range(len(queue)):
        bi, bj, ri, rj, d = queue.popleft()
        for next_d in next_dirs[d]:

            flag_red = False
            flag_blue = False
            next_bi, next_bj, next_ri, next_rj = bi, bj, ri, rj

            # ################# up
            if next_d == 0:
                if ri <= bi:
                    while True:
                        if board[next_ri - 1][next_rj] == '.':
                            next_ri -= 1
                            continue
                        elif board[next_ri - 1][next_rj] == 'O':
                            flag_red = True
                            break
                        else:
                            board[next_ri][next_rj] = 'R'
                            break

                    while True:
                        if board[next_bi - 1][next_bj] == '.':
                            next_bi -= 1
                            continue
                        elif board[next_bi - 1][next_bj] == 'O':
                            board[next_ri][next_rj] = '.'
                            flag_blue = True
                            break
                        else:
                            board[next_ri][next_rj] = '.'
                            if next_ri != ri or next_bi != bi:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

                else:
                    while True:
                        if board[next_bi - 1][next_bj] == '.':
                            next_bi -= 1
                            continue
                        elif board[next_bi - 1][next_bj] == 'O':
                            flag_blue = True
                            break
                        else:
                            board[next_bi][next_bj] = 'B'
                            break

                    if flag_blue:
                        continue

                    while True:
                        if board[next_ri - 1][next_rj] == '.':
                            next_ri -= 1
                            continue
                        elif board[next_ri - 1][next_rj] == 'O':
                            board[next_bi][next_bj] = '.'
                            flag_red = True
                            break
                        else:
                            board[next_bi][next_bj] = '.'
                            if next_ri != ri or next_bi != bi:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

            # ################# right
            elif next_d == 1:
                if rj >= bj:
                    while True:
                        if board[next_ri][next_rj + 1] == '.':
                            next_rj += 1
                            continue
                        elif board[next_ri][next_rj + 1] == 'O':
                            flag_red = True
                            break
                        else:
                            board[next_ri][next_rj] = 'R'
                            break

                    while True:
                        if board[next_bi][next_bj + 1] == '.':
                            next_bj += 1
                            continue
                        elif board[next_bi][next_bj + 1] == 'O':
                            board[next_ri][next_rj] = '.'
                            flag_blue = True
                            break
                        else:
                            board[next_ri][next_rj] = '.'
                            if next_rj != rj or next_bj != bj:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

                else:
                    while True:
                        if board[next_bi][next_bj + 1] == '.':
                            next_bj += 1
                            continue
                        elif board[next_bi][next_bj + 1] == 'O':
                            flag_blue = True
                            break
                        else:
                            board[next_bi][next_bj] = 'B'
                            break

                    if flag_blue:
                        continue

                    while True:
                        if board[next_ri][next_rj + 1] == '.':
                            next_rj += 1
                            continue
                        elif board[next_ri][next_rj + 1] == 'O':
                            board[next_bi][next_bj] = '.'
                            flag_red = True
                            break
                        else:
                            board[next_bi][next_bj] = '.'
                            if next_rj != rj or next_bj != bj:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

            # ################# down
            elif next_d == 2:
                if ri >= bi:
                    while True:
                        if board[next_ri + 1][next_rj] == '.':
                            next_ri += 1
                            continue
                        elif board[next_ri + 1][next_rj] == 'O':
                            flag_red = True
                            break
                        else:
                            board[next_ri][next_rj] = 'R'
                            break

                    while True:
                        if board[next_bi + 1][next_bj] == '.':
                            next_bi += 1
                            continue
                        elif board[next_bi + 1][next_bj] == 'O':
                            board[next_ri][next_rj] = '.'
                            flag_blue = True
                            break
                        else:
                            board[next_ri][next_rj] = '.'
                            if next_ri != ri or next_bi != bi:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

                else:
                    while True:
                        if board[next_bi + 1][next_bj] == '.':
                            next_bi += 1
                            continue
                        elif board[next_bi + 1][next_bj] == 'O':
                            flag_blue = True
                            break
                        else:
                            board[next_bi][next_bj] = 'B'
                            break

                    if flag_blue:
                        continue

                    while True:
                        if board[next_ri + 1][next_rj] == '.':
                            next_ri += 1
                            continue
                        elif board[next_ri + 1][next_rj] == 'O':
                            board[next_bi][next_bj] = '.'
                            flag_red = True
                            break
                        else:
                            board[next_bi][next_bj] = '.'
                            if next_ri != ri or next_bi != bi:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

            # ################# left
            else:
                if rj <= bj:
                    while True:
                        if board[next_ri][next_rj - 1] == '.':
                            next_rj -= 1
                            continue
                        elif board[next_ri][next_rj - 1] == 'O':
                            flag_red = True
                            break
                        else:
                            board[next_ri][next_rj] = 'R'
                            break

                    while True:
                        if board[next_bi][next_bj - 1] == '.':
                            next_bj -= 1
                            continue
                        elif board[next_bi][next_bj - 1] == 'O':
                            board[next_ri][next_rj] = '.'
                            flag_blue = True
                            break
                        else:
                            board[next_ri][next_rj] = '.'
                            if next_rj != rj or next_bj != bj:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

                else:
                    while True:
                        if board[next_bi][next_bj - 1] == '.':
                            next_bj -= 1
                            continue
                        elif board[next_bi][next_bj - 1] == 'O':
                            flag_blue = True
                            break
                        else:
                            board[next_bi][next_bj] = 'B'
                            break

                    if flag_blue:
                        continue

                    while True:
                        if board[next_ri][next_rj - 1] == '.':
                            next_rj -= 1
                            continue
                        elif board[next_ri][next_rj - 1] == 'O':
                            board[next_bi][next_bj] = '.'
                            flag_red = True
                            break
                        else:
                            board[next_bi][next_bj] = '.'
                            if next_rj != rj or next_bj != bj:
                                queue.append((next_bi, next_bj, next_ri, next_rj, next_d))
                            break

            if flag_blue:
                continue

            if flag_red:
                flag = True
                break

        if flag:
            break

    if flag:
        break
    else:
        cnt += 1

if flag:
    print(cnt)
else:
    print(-1)
