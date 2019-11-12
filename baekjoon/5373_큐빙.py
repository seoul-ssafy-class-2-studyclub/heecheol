import sys
sys.stdin = open('input.txt', 'r')


def rotate(side, dir):
    global front
    global left
    global right
    global up
    global down
    global back

    if side == 'F':
        if dir == '+':
            front[0], front[2] = front[2], front[0]
            front = list(map(list, zip(*front)))
            left[2][2], left[1][2], left[0][2], up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], \
            down[0][2], down[0][1], down[0][0] \
                = down[0][2], down[0][1], down[0][0], left[2][2], left[1][2], left[0][2], up[2][0], up[2][1], up[2][2], \
                  right[0][0], right[1][0], right[2][0]

        else:
            front = list(map(list, zip(*front)))
            front[0], front[2] = front[2], front[0]
            left[2][2], left[1][2], left[0][2], up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], \
            down[0][2], down[0][1], down[0][0] \
                = up[2][0], up[2][1], up[2][2], right[0][0], right[1][0], right[2][0], down[0][2], down[0][1], down[0][
                0], left[2][2], left[1][2], left[0][2]

    elif side == 'L':
        if dir == '+':
            left[0], left[2] = left[2], left[0]
            left = list(map(list, zip(*left)))
            back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], down[0][0], down[1][0], down[2][0] \
                = down[0][0], down[1][0], down[2][0], back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0]

        else:
            left = list(map(list, zip(*left)))
            left[0], left[2] = left[2], left[0]
            back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], \
            down[0][0], down[1][0], down[2][0] \
                = up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], down[0][0], down[1][0], down[2][0], back[2][2], back[1][2], back[0][2]

    elif side == 'R':
        if dir == '+':
            right[0], right[2] = right[2], right[0]
            right = list(map(list, zip(*right)))
            front[2][2], front[1][2], front[0][2], up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0], \
            down[2][2], down[1][2], down[0][2] \
                = down[2][2], down[1][2], down[0][2], front[2][2], front[1][2], front[0][2], up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0]

        else:
            right = list(map(list, zip(*right)))
            right[0], right[2] = right[2], right[0]
            front[2][2], front[1][2], front[0][2], up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0], \
            down[2][2], down[1][2], down[0][2] \
                = up[2][2], up[1][2], up[0][2], back[0][0], back[1][0], back[2][0], down[2][2], down[1][2], down[0][2], front[2][2], front[1][2], front[0][2]

    elif side == 'B':
        if dir == '+':
            back[0], back[2] = back[2], back[0]
            back = list(map(list, zip(*back)))
            right[2][2], right[1][2], right[0][2], up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0], \
            down[2][0], down[2][1], down[2][2] \
                = down[2][0], down[2][1], down[2][2], right[2][2], right[1][2], right[0][2], up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0]

        else:
            back = list(map(list, zip(*back)))
            back[0], back[2] = back[2], back[0]
            right[2][2], right[1][2], right[0][2], up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0], \
            down[2][0], down[2][1], down[2][2] \
                = up[0][2], up[0][1], up[0][0], left[0][0], left[1][0], left[2][0], down[2][0], down[2][1], down[2][2], right[2][2], right[1][2], right[0][2]

    elif side == 'U':
        if dir == '+':
            up[0], up[2] = up[2], up[0]
            up = list(map(list, zip(*up)))
            left[0][2], left[0][1], left[0][0], back[0][2], back[0][1], back[0][0], right[0][2], right[0][1], right[0][0], \
            front[0][2], front[0][1], front[0][0] \
                = front[0][2], front[0][1], front[0][0], left[0][2], left[0][1], left[0][0], back[0][2], back[0][1], back[0][0], right[0][2], right[0][1], right[0][0]

        else:
            up = list(map(list, zip(*up)))
            up[0], up[2] = up[2], up[0]
            left[0][2], left[0][1], left[0][0], back[0][2], back[0][1], back[0][0], right[0][2], right[0][1], right[0][0], \
            front[0][2], front[0][1], front[0][0] \
                = back[0][2], back[0][1], back[0][0], right[0][2], right[0][1], right[0][0], front[0][2], front[0][1], front[0][0], left[0][2], left[0][1], left[0][0],

    elif side == 'D':
        if dir == '+':
            down[0], down[2] = down[2], down[0]
            down = list(map(list, zip(*down)))
            left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], \
            back[2][0], back[2][1], back[2][2] \
                = back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], \

        else:
            down = list(map(list, zip(*down)))
            down[0], down[2] = down[2], down[0]
            left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], \
            right[2][2], back[2][0], back[2][1], back[2][2] \
                = front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2]


T = int(input())

for tc in range(1, T + 1):
    left = [['g'] * 3 for _ in range(3)]
    up = [['w'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]
    down = [['y'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]

    N = int(input())
    methods = list(input().split())

    for i in range(N):
        rotate(methods[i][0], methods[i][1])

    for i in range(3):
        print(''.join(up[i]))
