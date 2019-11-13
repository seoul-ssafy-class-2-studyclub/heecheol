import collections
import sys
sys.stdin = open('input.txt', 'r')


def step1(idx1, idx2):
    global max_num

    for right in range(1, N - idx2):
        for left in range(1, idx2 + 1):
            if left + right + idx1 < N and 2 * (left + right) > max_num:

                cnt = step2(idx1, idx2, left, right)

                if cnt > max_num:
                    max_num = cnt


def step2(idx1, idx2, left, right):
    arr = collections.deque([board[idx1][idx2]])

    for i in range(1, left + 1):
        if board[idx1 + i][idx2 - i] in arr:
            return -1
        else:
            arr.append(board[idx1 + i][idx2 - i])

    for i in range(1, right + 1):
        if board[idx1 + i][idx2 + i] in arr:
            return -1
        else:
            arr.append(board[idx1 + i][idx2 + i])

    for i in range(1, left + 1):
        if board[idx1 + right + i][idx2 + right - i] in arr:
            return -1
        else:
            arr.append(board[idx1 + right + i][idx2 + right - i])

    for i in range(1, right):
        if board[idx1 + left + i][idx2 - left + i] in arr:
            return -1
        else:
            arr.append(board[idx1 + left + i][idx2 - left + i])

    return 2 * (left + right)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    max_num = -1

    for i in range(N - 2):
        for j in range(1, N - 1):
            step1(i, j)

    print('#{} {}'.format(tc, max_num))
