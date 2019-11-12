import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    heights.sort(reverse=True)

    h = 0
    l = 99
    cnt = 0
    while True:
        if cnt == N:
            break
        elif heights[h] - heights[l] <= 1:
            print('==')
            break
        else:
            heights[h] -= 1
            heights[l] += 1
            if heights[h] < heights[h + 1]:
                h += 1
            else:
                h = 0
            if heights[l] > heights[l - 1]:
                l -= 1
            else:
                l = 99
        cnt += 1

    print('#{} {}'.format(tc, max(heights) - min(heights)))