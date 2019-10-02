import sys
sys.stdin = open('input.txt', 'r')


def how_much(m, fee):
    global total

    if fee >= total:
        return

    elif m >= 12:
        total = fee
        return

    else:
        if plan[m] == 0:
            how_much(m+1, fee)
        else:
            # d1
            how_much(m+1, fee + plan[m] * d1)
            # m1
            how_much(m+1, fee + m1)
            # m3
            how_much(m + 3, fee + m3)


for tc in range(1, int(input()) + 1):
    # fee
    d1, m1, m3, y1 = map(int, input().split())
    # plan
    plan = list(map(int, input().split()))

    total = y1
    i = 0
    how_much(0, 0)
    print('#{} {}'.format(tc, total))