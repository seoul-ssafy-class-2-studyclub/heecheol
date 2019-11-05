import sys
sys.stdin = open('input.txt', 'r')


def hee(idx, res):
    if idx == N:
        return
    else:
        res1 = res + score_list[idx]
        if not DP[idx].get(res1):
            DP[idx][res1] = 1
            hee(idx + 1, res1)
        if not DP[idx].get(res):
            hee(idx + 1, res)
            DP[idx][res] = 1


for tc in range(1, int(input()) + 1):
    N = int(input())
    score_list = list(map(int, input().split()))

    DP = [{} for _ in range(N)]
    hee(0, 0)
    print('#{} {}'.format(tc, len(DP[-1])))
