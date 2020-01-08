import collections
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
input_depth = list(map(int, input().split()))

max_depth = max(input_depth)
number_of_depth = [1] + [0] * max_depth

flag = True
for i in range(len(input_depth)):
    depth = input_depth[i]
    if number_of_depth[depth] + 1 > number_of_depth[depth - 1] * 2:
        flag = False
        break
    number_of_depth[depth] += 1

if flag is False:
    print(-1)

else:
    each_depth = [collections.deque() for _ in range(max_depth + 1)]
    d = max_depth

    for num in list(range(1, N + 1)):
        while True:
            if number_of_depth[d] > 0:
                number_of_depth[d] -= 1
                break
            if d == 0:
                d = max_depth
            else:
                d -= 1

        each_depth[d].append(num)

        if d == 0:
            d = max_depth
        else:
            d -= 1

    # print(each_depth)

    for i in range(max_depth, 1, -1):

        for j in range(2, len(each_depth[i]), 2):
            if each_depth[i][j] > each_depth[i - 1][j // 2]:
                each_depth[i][j], each_depth[i - 1][j // 2] = each_depth[i - 1][j // 2], each_depth[i][j]

    # print(each_depth)
    answer = [str(each_depth[0][0])]
    # print(input_depth)
    for idx in input_depth:
        answer.append(str(each_depth[idx].popleft()))

    print(' '.join(answer))
