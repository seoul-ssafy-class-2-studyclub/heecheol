import collections
import sys
sys.stdin = open('input.txt', 'r')


def permutation(arr, k):
    global perms

    if k == N - 1:
        perms.append(arr)
        return

    else:
        for i in range(4):
            if operations[i] > 0:
                operations[i] -= 1
                permutation(arr + [i], k + 1)
                operations[i] += 1
    return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # ['+', '-', '*', '//']
    operations = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    perms = collections.deque()
    permutation([], 0)

    max_result = -100000001
    min_result = 100000001

    for operation in perms:
        result = numbers[0]
        for i in range(N - 1):
            if operation[i] == 0:
                result += numbers[i + 1]

            elif operation[i] == 1:
                result -= numbers[i + 1]

            elif operation[i] == 2:
                result *= numbers[i + 1]

            else:
                result = int(result / numbers[i + 1])

        if result > max_result:
            max_result = result

        if result < min_result:
            min_result = result

    print('#{} {}'.format(tc, max_result - min_result))
