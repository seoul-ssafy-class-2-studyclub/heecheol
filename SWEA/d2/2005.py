T = int(input())

for t in range(1, T + 1):
    row_list = []
    N = int(input())

    print(f'#{t}')

    for row in range(1, N + 1):
        if row == 1:
            row_list.append(1)

        elif row == 2:
            row_list.append(1)

        else:        
            for i in range(1, row - 1):     # row = 3, for i in range(1, 3) # 1, 2
                row_list[i] = pre_list[i - 1] + pre_list[i]
            row_list.append(1)
        
        # deepcopy
        pre_list = list(map(str, row_list))
        pre_list = list(map(int, pre_list))
        
        string = ' '.join(map(str, row_list))
        print(string)
    