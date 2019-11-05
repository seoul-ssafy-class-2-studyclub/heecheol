import sys
sys.stdin = open('input.txt', 'r')


def in_border(i, j, k):
    cnt = 0
    for di in range(k):
        for dj in range(di-k+1, k-di):
            idx1, idx2 = i + di, j + dj
            if idx1 < N and 0 <= idx2 < N and board[idx1][idx2] == '1':
                cnt += 1

    for di in range(-k, 0):
        for dj in range(-di-k+1, di+k):
            idx1, idx2 = i + di, j + dj
            if 0 <= idx1 and 0 <= idx2 < N and board[idx1][idx2] == '1':
                cnt += 1

    return cnt

# main
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]

    max_num = 0
    flag = False
    for k in range(N+1, 0, -1):
        cost = k**2 + (k-1)**2
        for i in range(N):
            for j in range(N):
                num = in_border(i, j, k)
                if cost <= num * M and max_num < num:
                    max_num = num
                    if num == N**2:
                        flag = True
                        break
            if flag is True:
                break
        if flag is True:
            break
    print('#{} {}'.format(tc, max_num))





