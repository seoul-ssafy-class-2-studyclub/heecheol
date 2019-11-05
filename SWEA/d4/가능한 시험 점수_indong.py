import sys
sys.stdin = open('input.txt', 'r')


for case in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    L = sum(scores)
    dp = [True] + [False] * L
    res = 1
    vis = [0]

    for score in scores:
        for i in range(res):
            nxt = score + vis[i]
            if not dp[nxt]:
                dp[nxt] = True
                res += 1
                vis.append(nxt)
    # print(vis)
    print('#{} {}'.format(case, res))