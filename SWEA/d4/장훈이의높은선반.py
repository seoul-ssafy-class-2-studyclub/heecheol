def btk(i, value):
    global min_value
    if B <= value < min_value:
        min_value = value
        return
    if value > min_value or i == N:
        return
    else:
        btk(i+1, value + heights[i])
        btk(i+1, value)


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_value = 987654321
    btk(0, 0)
    print('#{} {}'.format(tc, min_value-B))