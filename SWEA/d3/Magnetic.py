# magnetic

for T in range(1, 11):
    size = int(input())
    table = []
    count = 0

    for i in range(size):
        table.append(list(map(int, input().split())))
    
    for j in range(size):   
        colume = []                                 
        for i in range(size):               # make a list
            if table[i][j] != 0:            # in each colume
                colume.append(table[i][j])  # without 0

        # N colume[0] colume[1] ... colume[n] S
        # N = 1, S = 2

        while len(colume) > 0:
            if colume[0] == 1:              # colume[0] must be 1 or 2
                colume.pop(0)
                if len(colume) == 0:
                    break
                elif colume[0] == 2:        # if there is S after N
                    colume.pop(0)
                    count += 1              # count it
                else:
                    pass

            elif colume[0] == 2:
                colume.pop(0)

    print(f'#{T} {count}')
