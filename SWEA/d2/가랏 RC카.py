for t in range(1, int(input())+1):
    v = 0
    distance = 0
    for i in range(int(input())):
        info = input().split()
        
        if len(info) == 1:
            distance += abs(v)
            print(f'0, v = {v}, d = {distance}')
        else:
            acc, diff = map(int, info)
            if acc == 1:
                v = v + diff
                distance += abs(v)
                print(f'1, v = {v}, d = {distance}')
            else:
                if v < diff:
                    v = 0
                else:                    
                    v = v - diff
                    distance += abs(v)
                    print(f'2, v = {v}, d = {distance}')

    print(f'#{t} {distance}')  