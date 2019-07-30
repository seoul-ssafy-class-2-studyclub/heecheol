for T in range(int(input())):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    if N == len(numbers):
        for i in range(N-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

        for i in range(N-2):
            if numbers[i] < numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

    # max_number = numbers[-1]
    # min_number = numbers[-2]
    print('#{} {}'.format(T+1, numbers[-1]-numbers[-2]))

