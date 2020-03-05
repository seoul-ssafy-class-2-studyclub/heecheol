import sys
sys.stdin = open('input.txt', 'r')


for tc in range(int(input())):
    answer = ['-'] * 3

    N = int(input())
    numbers = list(map(int, input().split()))
    value = sum(numbers) // 3

    flag = True
    while flag:

        flag1 = True
        i = 0

        while flag1:
            arr = numbers[:]
            temp = 0
            for j in range(len(arr) - i - 1, -i - 1, -1):
                if temp + arr[j] > value:
                    continue
                if temp + arr[j] < value:
                    temp += arr[j]
                    arr.pop(j)
                    continue
                if temp + arr[j] == value:
                    arr.pop(j)
                    flag1 = False
                    break
            else:
                i += 1

        arr.sort(reverse=True)
        flag2 = True


        break

    print('#{}'.format(tc + 1))
    print('\n'.join(answer))
