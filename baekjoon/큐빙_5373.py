import sys
sys.stdin = open('input.txt', 'r')


def turn(face, d):
    global up, down, front, back, left, right

    new = [['n'] * 3 for _ in range(3)]

    if face == 'F':
        if d == '+':
            for i in range(3):
                for j in range(3):
                    new[i][j] = front[2-j][i]
            front = [row[:] for row in new]
            up[2], [right[0][0], right[1][0], right[2][0]], [down[0][2], down[0][1], down[0][0]], [left[2][2], left[1][2], left[0][2]] = \
                [left[2][2], left[1][2], left[0][2]], up[2], [right[0][0], right[1][0], right[2][0]], [down[0][2], down[0][1], down[0][0]]
        else:
            for i in range(3):
                for j in range(3):
                    new[i][j] = front[j][2-i]
            front = [row[:] for row in new]
            up[2], [right[0][0], right[1][0], right[2][0]], [down[0][2], down[0][1], down[0][0]], [left[2][2], left[1][2], left[0][2]] = \
                [right[0][0], right[1][0], right[2][0]], [down[0][2], down[0][1], down[0][0]], [left[2][2], left[1][2], left[0][2]], up[2]

    elif face == 'R':
        if d == '+':
            for i in range(3):
                for j in range(3):
                    new[i][j] = right[2-j][i]
            right = [row[:] for row in new]
            [up[2][2], up[1][2], up[0][2]], [back[0][0], back[1][0], back[2][0]], [down[2][2], down[1][2], down[0][2]], [front[2][2], front[1][2], front[0][2]] \
                = [front[2][2], front[1][2], front[0][2]], [up[2][2], up[1][2], up[0][2]], [back[0][0], back[1][0], back[2][0]], [down[2][2], down[1][2], down[0][2]]
        else:
            for i in range(3):
                for j in range(3):
                    new[i][j] = right[j][2-i]
            right = [row[:] for row in new]
            [up[2][2], up[1][2], up[0][2]], [back[0][0], back[1][0], back[2][0]], [down[2][2], down[1][2], down[0][2]], [front[2][2], front[1][2], front[0][2]] \
                = [back[0][0], back[1][0], back[2][0]], [down[2][2], down[1][2], down[0][2]], [front[2][2], front[1][2], front[0][2]], [up[2][2], up[1][2], up[0][2]]

    elif face == 'B':
        if d == '+':
            for i in range(3):
                for j in range(3):
                    new[i][j] = back[2-j][i]
            back = [row[:] for row in new]
            [up[0][2], up[0][1], up[0][0]], [left[0][0], left[1][0], left[2][0]], [down[2][0], down[2][1], down[2][2]], [right[2][2], right[1][2], right[0][2]] \
                = [right[2][2], right[1][2], right[0][2]], [up[0][2], up[0][1], up[0][0]], [left[0][0], left[1][0], left[2][0]], [down[2][0], down[2][1], down[2][2]]
        else:
            for i in range(3):
                for j in range(3):
                    new[i][j] = back[j][2-i]
            back = [row[:] for row in new]
            [up[0][2], up[0][1], up[0][0]], [left[0][0], left[1][0], left[2][0]], [down[2][0], down[2][1], down[2][2]], [right[2][2], right[1][2], right[0][2]] \
                = [left[0][0], left[1][0], left[2][0]], [down[2][0], down[2][1], down[2][2]], [right[2][2], right[1][2], right[0][2]], [up[0][2], up[0][1], up[0][0]]

    elif face == 'L':
        if d == '+':
            for i in range(3):
                for j in range(3):
                    new[i][j] = left[2-j][i]
            left = [row[:] for row in new]
            [up[0][0], up[1][0], up[2][0]], [front[0][0], front[1][0], front[2][0]], [down[0][0], down[1][0], down[2][0]], [back[2][2], back[1][2], back[0][2]] \
                = [back[2][2], back[1][2], back[0][2]], [up[0][0], up[1][0], up[2][0]], [front[0][0], front[1][0], front[2][0]], [down[0][0], down[1][0], down[2][0]]
        else:
            for i in range(3):
                for j in range(3):
                    new[i][j] = left[j][2-i]
            left = [row[:] for row in new]
            [up[0][0], up[1][0], up[2][0]], [front[0][0], front[1][0], front[2][0]], [down[0][0], down[1][0], down[2][0]], [back[2][2], back[1][2], back[0][2]] \
                = [front[0][0], front[1][0], front[2][0]], [down[0][0], down[1][0], down[2][0]], [back[2][2], back[1][2], back[0][2]], [up[0][0], up[1][0], up[2][0]]

    elif face == 'U':
        if d == '+':
            for i in range(3):
                for j in range(3):
                    new[i][j] = up[2-j][i]
            up = [row[:] for row in new]
            [back[0][2], back[0][1], back[0][0]], [right[0][2], right[0][1], right[0][0]], [front[0][2], front[0][1], front[0][0]], [left[0][2], left[0][1], left[0][0]] \
                = [left[0][2], left[0][1], left[0][0]], [back[0][2], back[0][1], back[0][0]], [right[0][2], right[0][1], right[0][0]], [front[0][2], front[0][1], front[0][0]]

        else:
            for i in range(3):
                for j in range(3):
                    new[i][j] = up[j][2-i]
            up = [row[:] for row in new]
            [back[0][2], back[0][1], back[0][0]], [right[0][2], right[0][1], right[0][0]], [front[0][2], front[0][1], front[0][0]], [left[0][2], left[0][1], left[0][0]] \
                = [right[0][2], right[0][1], right[0][0]], [front[0][2], front[0][1], front[0][0]], [left[0][2], left[0][1], left[0][0]], [back[0][2], back[0][1], back[0][0]]

    else:
        if d == '+':
            for i in range(3):
                for j in range(3):
                    new[i][j] = down[2-j][i]
            down = [row[:] for row in new]
            front[2], right[2], back[2], left[2] = left[2], front[2], right[2], back[2]
        else:
            for i in range(3):
                for j in range(3):
                    new[i][j] = down[j][2-i]
            down = [row[:] for row in new]
            front[2], right[2], back[2], left[2] = right[2], back[2], left[2], front[2]


T = int(input())
for _ in range(T):
    N = int(input())

    up = [['w'] * 3 for _ in range(3)]
    down = [['y'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]

    for info in list(input().split()):
        turn(info[0], info[1])

    print(''.join(up[0]))
    print(''.join(up[1]))
    print(''.join(up[2]))
