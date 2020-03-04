import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
answer = ['#'] * T

for tc in range(T):
    N = int(input())
    heights = list(map(int, input().split()))

    # sort
    heights.sort()

    heights.insert(0, heights[0])
    heights.append(heights[-1])

    diff = 0
    for idx in range(2, N + 2):
        if heights[idx] - heights[idx - 2] > diff:
            diff = heights[idx] - heights[idx - 2]

    answer[tc] = '#{} {}'.format(tc + 1, diff)

print('\n'.join(answer))
