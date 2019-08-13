for tc in range(10):
    N = int(input())
    ladder = []
 
    for row in range(100):
        ladder.append(input().split())
 
    row = 99
    col = ladder[row].index('2')
    flag = 0

    while row > 0:
        if flag == 0:
            if col != 99 and ladder[row][col+1] == '1':
                col += 1
                flag = 1
            elif col != 0 and ladder[row][col-1] == '1':
                col -= 1
                flag = 2
            else:
                row -= 1
        elif flag == 1:
            if ladder[row-1][col] == '1':
                row -= 1
                flag = 0
            else:
                col += 1
        else:
            if ladder[row-1][col] == '1':
                row -= 1
                flag = 0
            else:
                col -= 1
             
    print(f'#{N} {col}')