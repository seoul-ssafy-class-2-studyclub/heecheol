import sys
sys.stdin = open('input.txt', 'r')


def cart(s, summ, cnt):
    global minn
    visit[s] = True
    if summ >= minn:
        pass
    elif cnt == N-1:
        summ += board[s][0]
        if summ < minn:
            minn = summ
    else:
        for i in range(N):
            if visit[i] is False:
                temp_sum = summ + board[s][i]
                cart(i, temp_sum, cnt+1)
                visit[i] = False


for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * N
    minn = 999999

    cart(0, 0, 0)
    print('#{} {}'.format(tc, minn))