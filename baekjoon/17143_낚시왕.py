import heapq
import sys
sys.stdin = open('input.txt', 'r')

R, C, M = map(int, input().split())     # row, col, amount
sharks = [list(map(int, input().split())) for _ in range(M)]

# nxt = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
# d_change = {1: 2, 2: 1, 3: 4, 4: 3}
total = 0
man = 0     # person location

while True:

    # step1 이동
    man += 1
    if man > C:
        break

    if len(sharks) == 0:
        break

    # step2 낚시
    same_col = []

    for i in range(len(sharks)):    # 같은 줄 상어 찾기
        r, c, s, d, z = sharks[i]
        if c == man:
            heapq.heappush(same_col, (r, z, i))

    if len(same_col) != 0:      # 잡을 상어가 있다면
        caught = heapq.heappop(same_col)
        sharks.pop(caught[2])   # 해당 index 의 상어 pop
        total += caught[1]      # + kilogram

    # step3 상어 이동, check board
    board = [[(0, 0, 0)] * (C + 1) for _ in range(R + 1)]
    eaten = []

    if len(sharks) == 0:
        break

    for i in range(len(sharks)):
        r, c, s, d, z = sharks[i]
        if d == 1:
            move = s % (2 * R - 2)
            tr = r - move
            if tr < 1:
                r = 2 - tr
                if r > R:
                    r = 2 * R - r
                else:
                    d = 2
            else:
                r = tr

        elif d == 2:
            move = s % (2 * R - 2)
            tr = r + move
            if tr > R:
                r = 2 * R - tr
                if r < 1:
                    r = 2 - r
                else:
                    d = 1
            else:
                r = tr

        elif d == 3:
            move = s % (2 * C - 2)
            tc = c + move
            if tc > C:
                c = 2 * C - tc
                if c < 1:
                    c = 2 - c
                else:
                    d = 4
            else:
                c = tc

        else:
            move = s % (2 * C - 2)
            tc = c - move
            if tc < 1:
                c = 2 - tc
                if c > C:
                    c = 2 * C - c
                else:
                    d = 3
            else:
                c = tc

        sharks[i] = (r, c, s, d, z)

        if board[r][c] == (0, 0, 0):
            board[r][c] = (z, i, d)

        elif z > board[r][c][0]:
            eaten.append(board[r][c][1])
            board[r][c] = (z, i, d)

        else:
            eaten.append(i)

    # 잡아먹힌 상어 제거
    for i in range(len(eaten)):
        eaten.sort()
        idx = eaten.pop()
        sharks.pop(idx)

print(total)
