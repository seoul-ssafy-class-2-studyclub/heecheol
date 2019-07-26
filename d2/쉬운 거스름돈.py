for t in range(int(input())):
    N = int(input())

    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    print(f'#{t + 1}')
    for money in money_list:
        value = N // money
        N = N % money
        print(value, end=' ')
    print()
