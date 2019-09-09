import sys
import itertools
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    numbers = list(itertools.combinations(num_list, 2))
    L = N*(N-1)//2
    for i in range(L):
        numbers[i] = numbers[i][0] * numbers[i][1]

    numbers.sort(reverse=True)
    for i in range(L):
        number = list(str(numbers[i]))
        if number == sorted(number):
            if len(number) > 1:
                print('#{} {}'.format(tc, ''.join(number)))
                break
    else:
        print('#{} -1'.format(tc))
