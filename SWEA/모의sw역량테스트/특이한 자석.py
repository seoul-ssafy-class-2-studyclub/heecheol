import collections
import sys
sys.stdin = open('input.txt', 'r')


# step1
def check_left_right(n, d):
    n1 = n2 = n
    d1 = d2 = d
    move = [(n, d)]
    # left
    while n1 > 0:
        if gears[n1 - 1][2] != gears[n1][6]:
            d1 *= -1
            move.append((n1 - 1, d1))
            n1 -= 1
        else:
            break
    while n2 < 3:
        if gears[n2][2] != gears[n2 + 1][6]:
            d2 *= -1
            move.append((n2 + 1, d2))
            n2 += 1
        else:
            break
    return move


T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    gears = [collections.deque() for _ in range(4)]

    for i in range(4):
        gears[i].extend(list(map(int, input().split())))

    # print(gears)
    for _ in range(K):
        gn, di = map(int, input().split())
        gears_rotated = check_left_right(gn - 1, di)
        for gear, direction in gears_rotated:
            gears[gear].rotate(direction)

    result = 0
    for i in range(4):
        result += gears[i][0] * (2 ** i)

    print('#{} {}'.format(tc, result))


