import sys
sys.stdin = open('input.txt', 'r')


def check_sub(ii, jj, honey, revenue, cnt):
    global max_revenue
    if honey > C:
        return
    elif cnt == M:
        if revenue > max_revenue:
            max_revenue = revenue
            board2[N * ii + jj - 1] = max_revenue
        return
    else:
        check_sub(ii, jj + 1, honey + board[ii][jj], revenue + board[ii][jj] ** 2, cnt + 1)
        check_sub(ii, jj + 1, honey, revenue, cnt + 1)


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    board2 = [0] * (N * N)

    for i in range(N):
        for j in range(N-M+1):
            max_revenue = 0
            check_sub(i, j, 0, 0, 0)

    max_total = 0
    for i in range(N * N - M):
        total = board2[i] + max(board2[i + M:])
        if total > max_total:
            max_total = total
    print('#{} {}'.format(tc, max_total))
