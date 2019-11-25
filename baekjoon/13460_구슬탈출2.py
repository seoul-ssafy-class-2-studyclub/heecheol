import collections
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
beads = []

for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            beads.append((i, j, 'R'))
            board[i][j] = '.'
        elif board[i][j] == 'B':
            beads.append((i, j, 'B'))
            board[i][j] = '.'
    if len(beads) == 2:
        break
# print(beads)
nxt_ds = {0: [2, 3], 1: [2, 3], 2: [0, 1], 3: [0, 1], 4: [0, 1, 2, 3]}
min_value = 11

# queue => while
# ((1, 3, 'B'), (3, 1, 'R'), 4)
queue = collections.deque([(beads, 4, 1)])
finish = False

while queue:
    two_beads, D, cnt = queue.popleft()
    if cnt > 10:
        break
    for d in nxt_ds[D]:
        in_hole = []
        board2 = [row[:] for row in board]
        if d == 0:  # left
            two_beads.sort()
            temp = []
            for bead in two_beads:
                idx1, idx2, color = bead
                while True:
                    if board2[idx1][idx2 - 1] == 'O':
                        in_hole.append(color)
                        break
                    elif board2[idx1][idx2 - 1] == '.':
                        idx2 -= 1
                        continue
                    else:
                        temp.append((idx1, idx2, color))
                        board2[idx1][idx2] = color
                        break

        elif d == 1:    # right
            two_beads.sort(reverse=True)
            temp = []
            for bead in two_beads:
                idx1, idx2, color = bead
                while True:
                    if board2[idx1][idx2 + 1] == 'O':
                        in_hole.append(color)
                        break
                    elif board2[idx1][idx2 + 1] == '.':
                        idx2 += 1
                        continue
                    else:
                        temp.append((idx1, idx2, color))
                        board2[idx1][idx2] = color
                        break

        elif d == 2:    # down
            two_beads.sort(reverse=True)
            temp = []
            for bead in two_beads:
                idx1, idx2, color = bead
                while True:
                    if board2[idx1 + 1][idx2] == 'O':
                        in_hole.append(color)
                        break
                    elif board2[idx1 + 1][idx2] == '.':
                        idx1 += 1
                        continue
                    else:
                        temp.append((idx1, idx2, color))
                        board2[idx1][idx2] = color
                        break

        elif d == 3:
            two_beads.sort()
            temp = []
            for bead in two_beads:
                idx1, idx2, color = bead
                while True:
                    if board2[idx1 - 1][idx2] == 'O':
                        in_hole.append(color)
                        break
                    elif board2[idx1 - 1][idx2] == '.':
                        idx1 -= 1
                        continue
                    else:
                        temp.append((idx1, idx2, color))
                        board2[idx1][idx2] = color
                        break

        if len(in_hole) == 0:
            queue.append((temp, d, cnt + 1))
        elif 'B' in in_hole:
            continue
        else:
            finish = True
            break
    if finish is True:
        break
if finish is True:
    print(cnt)
else:
    print(-1)

