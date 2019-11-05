import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    idx = 2
    cnt = 0
    while idx < (N-2):
        max_near = max([heights[idx-2], heights[idx-1], heights[idx+1], heights[idx+2]])
        if heights[idx] > max_near:
            cnt += heights[idx] - max_near
            idx += 3
        else:
            idx += 1
    print('#{} {}'.format(tc, cnt))