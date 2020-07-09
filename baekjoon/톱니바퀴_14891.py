import sys
sys.stdin = open('input.txt', 'r')

import collections


def check_left(n, d):
    will_turn = [(n, d)]
    while n > 0:
        if gears[n][6] == gears[n-1][2]:
            return will_turn
        else:
            d *= -1
            n -= 1
            will_turn.append((n, d))
    return will_turn


def check_right(n, d):
    will_turn = []
    while n < 3:
        if gears[n][2] == gears[n+1][6]:
            return will_turn
        else:
            d *= -1
            n += 1
            will_turn.append((n, d))
    return will_turn


gears = [collections.deque(list(input())) for _ in range(4)]
K = int(input())
point = 0
for _ in range(K):
    input_gear_number, input_direction = map(int, input().split())
    input_gear_number -= 1

    left_gears = check_left(input_gear_number, input_direction)
    right_gears = check_right(input_gear_number, input_direction)

    for num, D in left_gears:
        gears[num].rotate(D)

    for num, D in right_gears:
        gears[num].rotate(D)

for i in range(4):
    if gears[i][0] == '1':
        point += 2 ** i

print(point)

