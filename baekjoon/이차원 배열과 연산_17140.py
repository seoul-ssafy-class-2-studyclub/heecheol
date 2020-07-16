import sys
sys.stdin = open('input.txt', 'r')
from pprint import pprint
import collections


def r_calculation():
    for i in range(R):
        rows[i] = collections.defaultdict(int)
        for j in range(C):
            if board[i][j] == 0:
                continue
            rows[i][board[i][j]] += 1

    return max(len(value) for value in rows.values()) * 2


def c_calculation():
    for j in range(C):
        cols[j] = collections.defaultdict(int)
        for i in range(R):
            if board[i][j] == 0:
                continue
            cols[j][board[i][j]] += 1

    return max(len(value) for value in cols.values()) * 2


def r_insert():
    for i in range(R):
        row = []
        for key, value in rows[i].items():
            row.append((value, key))
        row.sort()

        for j in range(len(row)):
            board[i][2*j] = row[j][1]
            board[i][2*j + 1] = row[j][0]


def c_insert():
    for j in range(C):
        col = []
        for key, value in cols[j].items():
            col.append((value, key))
        col.sort()

        for i in range(len(col)):
            board[2*i][j] = col[i][1]
            board[2*i + 1][j] = col[i][0]


r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]

R = C = 3
time = 0
while True:
    if r <= R and c <= C:
        if board[r-1][c-1] == k:
            break

    if R >= C:
        rows = {}
        C = r_calculation()
        if C > 100:
            C = 100
        board = [[0] * C for _ in range(R)]
        r_insert()

    else:
        cols = {}
        R = c_calculation()
        if R > 100:
            R = 100
        board = [[0] * C for _ in range(R)]
        c_insert()

    time += 1
    if time > 100:
        time = -1
        break

print(time)
