from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def fishing(man):
    for row in range(1, R+1):
        if board[row][man] != 0:
            size = board[row][man]
            shark_alive[size] = False
            return size
    return 0


def next_position(size):
    idx1, idx2 = shark_index[size]
    direction = shark_info[size]['d']
    speed = shark_info[size]['s']
    if direction == 1:
        nxt1 = idx1 - speed
        if nxt1 < 1:
            nxt1 = 2 - nxt1
            if nxt1 > R:
                nxt1 = 2*R - nxt1
            else:
                shark_info[size]['d'] = 2
        return nxt1, idx2
    elif direction == 2:
        nxt1 = idx1 + speed
        if nxt1 > R:
            nxt1 = 2*R - nxt1
            if nxt1 < 1:
                nxt1 = 2 - nxt1
            else:
                shark_info[size]['d'] = 1
        return nxt1, idx2
    elif direction == 3:
        nxt2 = idx2 + speed
        if nxt2 > C:
            nxt2 = 2*C - nxt2
            if nxt2 < 1:
                nxt2 = 2 - nxt2
            else:
                shark_info[size]['d'] = 4
        return idx1, nxt2
    else:
        nxt2 = idx2 - speed
        if nxt2 < 1:
            nxt2 = 2 - nxt2
            if nxt2 > C:
                nxt2 = 2*C - nxt2
            else:
                shark_info[size]['d'] = 3
        return idx1, nxt2


def moving():
    for size, alive in shark_alive.items():
        if alive:
            nxt1, nxt2 = next_position(size)
            if size > board[nxt1][nxt2]:
                shark_alive[board[nxt1][nxt2]] = False
                board[nxt1][nxt2] = size
                shark_index[size] = [nxt1, nxt2]
            else:
                shark_alive[size] = False


R, C, M = map(int, input().split())
board = [[0] * (1+C) for _ in range(R+1)]

shark_alive = {
    0: False
}
shark_index = {}
shark_info = {}

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r][c] = z
    shark_alive[z] = True
    shark_index[z] = [r, c]
    if d <= 2:
        shark_info[z] = {
            's': s % (2 * R - 2),
            'd': d
        }
    else:
        shark_info[z] = {
            's': s % (2 * C - 2),
            'd': d
        }

result = 0
for idx in range(1, C+1):
    result += fishing(idx)
    board = [[0] * (1+C) for _ in range(R+1)]
    moving()

print(result)
