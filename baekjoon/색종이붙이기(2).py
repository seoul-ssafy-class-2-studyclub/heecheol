import sys
sys.stdin = open('input.txt', 'r')


def check(x, y):
    print(x, y)
    global cnt
    for size in range(1, 11):
        flag1 = True
        for dx in range(size):
            for dy in range(size):
                nx = x + dx
                ny = y + dy
                if nx < 10 and ny < 10:
                    if board[nx][ny] == '0':
                        size -= 1
                        flag1 = False
                        break
            if flag1 is False:
                break
        if flag1 is False:
            break
    for i in range(size):
        for j in range(size):
            board[x + i][y + j] = '0'
    sizes.append(size)


need = [[[1]],
        [[1, 1, 1, 1], [2]],
        [[3], [1, 1, 1, 1, 1, 2]],
        [[4], [2, 2, 2, 2]],
        [[5], [3, 2, 2, 2, 1, 1, 1, 1]],
        [[4, 2, 2, 2, 2, 2], [3, 3, 3, 3]],
        [[4, 3, 3, 2, 2, 2, 1, 1, 1], [5, 2, 2, 2, 2, 2, 1, 1, 1, 1]],
        [[4, 4, 4, 4], [5, 3, 3, 3, 2, 2, 1, 1, 1, 1]],
        [[5, 4, 4, 3, 2, 2, 2, 1, 1, 1]],
        [[5, 5, 5, 5]]]


board = [input().split() for _ in range(10)]
visit = [[False] * 10 for _ in range(10)]
cnt = 0
sizes = []
paper = [0, 5, 5, 5, 5, 5]

flag2 = True
for i in range(10):
    for j in range(10):
        if board[i][j] == '1':
            check(i, j)

print(board)
print(sizes)