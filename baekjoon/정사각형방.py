import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    flag1 = False   # find start_point
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                flag1 = True
                break
        if flag1 is True:
            break
    # start_point = board[i][j]

    adj_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    num = 1
    cnt = 1
    max_cnt = 0
    that_num = 0
    while num < N**2:
        print(num)
        for adj in adj_list:
            nxt_i, nxt_j = i + adj[0], j + adj[1]
            if 0 <= nxt_i < N and 0 <= nxt_j < N and board[nxt_i][nxt_j] == num + 1:
                i, j = nxt_i, nxt_j
                num += 1
                cnt += 1
                if num == N**2:
                    if cnt > max_cnt:
                        max_cnt = cnt
                        that_num = num - cnt + 1
                break
        else:
            if cnt > max_cnt:
                max_cnt = cnt
                that_num = num - cnt + 1
            flag2 = False
            # print(num, cnt, 2)
            for row in range(N):
                for col in range(N):
                    if board[row][col] == num + 1:
                        i, j = row, col
                        num += 1
                        cnt = 1
                        flag2 = True
                        break
                if flag2 is True:
                    break

    print(f'#{tc} {that_num} {max_cnt}')
