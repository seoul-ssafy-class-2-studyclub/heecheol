
def miro(x, y):
    visit[x][y] = True

    for i in range(4):
        ix = x + near[i][0]
        iy = y + near[i][1]
        if 0 <= ix < row and 0 <= iy < row:
            if board[ix][iy] == '3':
                return 1

            elif board[ix][iy] == '0' and visit[ix][iy] == False:
                temp = miro(ix, iy)
                if temp == 1:
                    return 1

    if x == si and y == sj:
        return 0

TC = int(input())
for tc in range(1, TC+1):
    row = int(input())
    board = [list(input()) for r in range(row)]
    visit = [[False]*row for r in range(row)]

    si = sj = 0
    sflag = False
    for i in range(row):
        for j in range(row):
            if board[i][j] == '2':
                si = i
                sj = j
                sflag = True
                break
        if sflag == True:
            break

    near = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    result = miro(si, sj)
    print('#{} {}'.format(tc, result))