a, b = map(int, input().split())
if 1 <= a <= 3 and 1 <= b <= 3:
    if a - b == 1 or a - b == -2:
        print('A')
    else:
        print('B')