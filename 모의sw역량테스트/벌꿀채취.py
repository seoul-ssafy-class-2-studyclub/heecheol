import itertools
import sys
sys.stdin = open('input.txt', 'r')


def check(i, j):
    part = board[i][j:j+M]


for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    subset = list(itertools.combinations(list(range(N))))

    for i in range(N):
        for j in range(N-M+1):
            check(i, j)