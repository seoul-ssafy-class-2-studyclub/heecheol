def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

for T in range(int(input())):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    max_M = sum_list(numbers[0:M])
    min_M = sum_list(numbers[0:M])

    for i in range(1, N-M+1):
        sum_M = sum_list(numbers[i:i+M])
        if sum_M > max_M:
            max_M = sum_M
        elif sum_M < min_M:
            min_M = sum_M
            
    print('#{} {}'.format(T+1, max_M - min_M))