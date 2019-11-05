# 불면증 치료법

for t in range(int(input())):

    N = int(input())
    num_list = []
    set_list = []
    k = 0

    while len(set_list) < 10:       # if set_list = [0, 1, 2, ... , 9] => len(set_list) = 10
        k += 1
        number = k * N              # 1N, 2N, 3N, ...
        str_number = str(number)    

        for num in str_number:
            num_list.append(num)
            set_list = set(num_list)

    print(f'#{t + 1} {number}')
