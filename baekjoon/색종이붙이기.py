from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def put(x, y):

    for i in range(x, 10):
        for j in range(10):
            if board[i][j] == '1':
                return

def check_size(x, y):
    flag = True
    for size in range(1, 11):
        for dx in range(size):
            for dy in range(size):
                nxt_x = x + dx
                nxt_y = y + dy
                if nxt_x < 10 and nxt_y < 10:
                    if board[nxt_x][nxt_y] == '0':
                        flag = False
                        size -= 1
                        break
            if flag is False:
                break
        if flag is False:
            break

    for dx in range(size):
        for dy in range(size):
            board[x + dx][y + dy] = '0'
    return size


board = [input().split() for _ in range(10)]
sizes = []
cnt = 0

for i in range(10):
    for j in range(10):
        if board[i][j] == '1':
            sizes.append(check_size(i, j))

print(sizes)
