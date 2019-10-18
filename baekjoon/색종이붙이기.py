import sys
sys.stdin = open('input.txt', 'r')


def check(ix, iy):
    for size in range(1, 5):
        for i in range(size):
            for j in range(size):
                if board[ix + i][iy + j] == '0':
                    return size
    return size + 1


def cover(ix, iy, size):
    for i in range(size):
        for j in range(size):
            board[ix + i][iy + j] = '0'


def reveal(ix, iy, size):
    for i in range(size):
        for j in range(size):
            board[ix + i][iy + j] = '1'


def solution(row, cnt):
    global possible
    global min_paper

    if cnt > min_paper:
        return

    else:
        for i in range(row, 10):
            for j in range(10):
                if board[i][j] == '1':
                    max_size = check(i, j)
                    for p in range(max_size):
                        if p == 0:
                            amount[0] -= 1
                            if amount[0] >= 0:
                                board[i][j] = '0'
                                solution(i, cnt + 1)
                                board[i][j] = '1'
                            else:
                                amount[0] += 1
                                continue
                        else:
                            amount[p] -= 1
                            if amount[p] >= 0:
                                cover(i, j, p)
                                solution(i, cnt + 1)
                                reveal(i, j, p)
                            else:
                                amount[p] += 1
                el

        if cnt <= min_paper:
            min_paper = cnt


board = [input().split() for _ in range(10)]
total = 0   # 필요한 색종이의 수

min_paper = 25
amount = [5] * 5

solution(0, 0)
print(min_paper)