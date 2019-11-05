import itertools
import sys
sys.stdin = open('input.txt', 'r')


def check(row, pb):
    global max_pb

    if pb <= max_pb:
        return
    elif row == N:
        max_pb = pb
        return
    else:
        for col in range(N):
            if row == 0:
                pb = 1

            if visited[col] is False:
                pb2 = pb * board[row][col]
                if pb2 >= max_pb:
                    visited[col] = True
                    check(row + 1, pb2)
                    visited[col] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(lambda x: int(x) / 100, input().split())) for _ in range(N)]

    visited = [False] * N
    max_pb = 0
    check(0, 1)

    print('#{} {:.6f}'.format(tc, max_pb*100))
