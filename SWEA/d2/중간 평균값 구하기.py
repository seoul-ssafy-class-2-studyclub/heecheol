T = int(input())

for t in range(1, T + 1):

    num_list = list(map(int, input().split()))

    if len(num_list) == 10:
        num_list.sort()
        num_list = num_list[1:9]            # slice()

        average = sum(num_list) / 8
        print(f'#{t} {round(average)}')     # round()

    else:
        print('----------')
