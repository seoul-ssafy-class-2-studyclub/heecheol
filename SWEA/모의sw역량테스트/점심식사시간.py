import itertools
import collections
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                people.append((i, j))
            elif board[i][j] > 1:
                stair.append((i, j, board[i][j]))

    p_len = len(people)
    stair_0 = [0] * p_len
    stair_1 = [0] * p_len
    for i in range(p_len):
        stair_0[i] = abs(people[i][0] - stair[0][0]) + abs(people[i][1] - stair[0][1])
        stair_1[i] = abs(people[i][0] - stair[1][0]) + abs(people[i][1] - stair[1][1])

    min_time = 987654321

    for i in range(p_len + 1):
        p_zeros = list(itertools.combinations(list(range(p_len)), i))

        for p_zero in p_zeros:
            d_s_0 = []
            d_s_1 = []
            for j in range(p_len):
                if j in p_zero:
                    d_s_0.append(stair_0[j])
                else:
                    d_s_1.append(stair_1[j])
            d_s_0.sort()
            d_s_1.sort()

            in_s_0 = collections.deque()
            in_s_1 = collections.deque()

            time = 0

            while True:
                if time > min_time:
                    break

                if len(d_s_0) == 0 and len(d_s_1) == 0 and len(in_s_0) == 0 and len(in_s_1) == 0:
                    break

                else:
                    time += 1

                    for p in range(len(d_s_0) - 1, -1, -1):
                        if d_s_0[p] == 0:
                            in_s_0.append((d_s_0.pop(p)))
                        else:
                            d_s_0[p] -= 1
                    for p in range(len(d_s_1) - 1, -1, -1):
                        if d_s_1[p] == 0:
                            in_s_1.append((d_s_1.pop(p)))
                        else:
                            d_s_1[p] -= 1

                    idx_s_0 = 0
                    while idx_s_0 < 3:
                        if idx_s_0 >= len(in_s_0):
                            break
                        if in_s_0[idx_s_0] == stair[0][2]:
                            in_s_0.popleft()
                        else:
                            in_s_0[idx_s_0] += 1
                            idx_s_0 += 1

                    idx_s_1 = 0
                    while idx_s_1 < 3:
                        if idx_s_1 >= len(in_s_1):
                            break
                        if in_s_1[idx_s_1] == stair[1][2]:
                            in_s_1.popleft()
                        else:
                            in_s_1[idx_s_1] += 1
                            idx_s_1 += 1
                # print(time)
                # print('stair_0')
                # print(d_s_0)
                # print(in_s_0)
                # print('stair_1')
                # print(d_s_1)
                # print(in_s_1)
                # print('-----------------')
            if time < min_time:
                min_time = time

    print(min_time)
