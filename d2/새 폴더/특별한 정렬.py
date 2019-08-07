for tc in range(int(input())):
    N = int(input())    # length
    numbers = list(map(int, input().split()))

    for i in range(10):
        part = numbers[i:]
        if i % 2 == 0:
            max_index = i
            for j in range(i + 1, N):
                if numbers[j] > numbers[max_index]:
                    max_index = j
            numbers[i], numbers[max_index] = numbers[max_index], numbers[i]
        else:
            min_index = i
            for j in range(i + 1, N):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    numbers = ' '.join(list(map(str,numbers[:10])))
    
    print(f'#{tc+1} {numbers}')


