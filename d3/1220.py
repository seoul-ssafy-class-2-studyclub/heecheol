# magnetic

for T in range(1, 11):
    size = int(input())
    table = []
    count = 0

    for i in range(size):
        table.append(list(map(int, input().split())))
    
    for j in range(size):   
        colume = []
        for i in range(size):
            if table[i][j] != 0:
                colume.append(table[i][j])
        # print(colume)

        while len(colume) > 0:
            if colume[0] == 1:
                colume.pop(0)
                if len(colume) == 0:
                    break
                elif colume[0] == 2:
                    colume.pop(0)
                    count += 1
                else:
                    pass

            elif colume[0] == 2:
                colume.pop(0)
    print(f'#{T} {count}')
