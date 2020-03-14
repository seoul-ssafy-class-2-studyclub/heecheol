import sys
sys.stdin = open('input.txt', 'r')

import collections


T = int(input())

for tc in range(T):
    N = int(input())
    board = [input().split() for _ in range(N)]

    front_back = {}
    back_front = {}

    for i in range(N):
        for j in range(N):
            if board[i][j] == '0':
                continue

            right = down = 1
            while True:
                if j + right == N or board[i][j + right] == '0':
                    break
                right += 1
            while True:
                if i + down == N or board[i + down][j] == '0':
                    break
                down += 1

            for ii in range(i, i + down):
                for jj in range(j, j + right):
                    board[ii][jj] = '0'

            front_back[down] = right
            back_front[right] = down

    order = [down, right]

    # move to front
    while True:
        if back_front.get(order[0]) is None:
            break
        order.insert(0, back_front[order[0]])

    # move to back
    while True:
        if front_back.get(order[-1]) is None:
            break
        order.append(front_back[order[-1]])

    min_total = float('inf')

    queue = collections.deque()
    queue.append([order, 0])

    while queue:
        arr, temp = queue.popleft()
        if temp >= min_total:
            continue

        if len(arr) == 3:
            temp2 = arr[0] * arr[1] * arr[2]
            if temp + temp2 < min_total:
                min_total = temp + temp2
            continue

        for mid in range(1, len(arr) - 1):
            temp2 = arr[mid - 1] * arr[mid] * arr[mid + 1]
            if temp + temp2 >= min_total:
                continue
            n_arr = arr[:mid] + arr[mid + 1:]
            queue.append([n_arr, temp + temp2])

    print('#{} {}'.format(tc + 1, min_total))
