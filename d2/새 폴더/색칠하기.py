for tc in range(int(input())):
    board = [[0 for i in range(10)] for i in range(10)]

    for N in range(int(input())):
        left1, left2, right1, right2, color = map(int, input().split())
        for i in range(left1, right1+1):
            for j in range(left2, right2+1):
                board[i][j] += color
    
    cnt = 0
    for i in range(10):
        for j in range(10):
            if board[i][j] == 3:
                cnt += 1
   
    print(f'#{tc+1} {cnt}')
