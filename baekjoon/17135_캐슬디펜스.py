from pprint import pprint
import itertools
import sys
sys.stdin = open('input.txt', 'r')


def step1(p_row, c1, c2, c3):
    global cnt
    enemies = set()
    for p_col in [c1, c2, c3]:
        flag = False
        for d in range(1, D + 1):
            for c in range(-d + 1, d):
                for r in range(1, d + 1):
                    if r + abs(c) == d:
                        nxt1, nxt2 = p_row - r, p_col + c
                        if 0 <= nxt1 and 0 <= nxt2 < M:
                            if board[nxt1][nxt2] == 1:
                                enemies.add((nxt1, nxt2))
                                flag = True
                                break
                if flag is True:
                    break
            if flag is True:
                break
    for e1, e2 in list(enemies):
        board[e1][e2] = 0
        cnt += 1


N, M, D = map(int, input().split())
board2 = [list(map(int, input().split())) for _ in range(N)]

max_kill = 0
positions = list(itertools.combinations(list(range(M)), 3))
for position in positions:
    board = [row[:] for row in board2]
    col1, col2, col3 = position
    cnt = 0
    row = N
    while row >= 0:
        step1(row, col1, col2, col3)
        row -= 1
    if cnt > max_kill:
        max_kill = cnt
print(max_kill)
