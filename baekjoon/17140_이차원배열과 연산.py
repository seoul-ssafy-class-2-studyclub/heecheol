import sys
sys.stdin = open('input.txt', 'r')


r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(3)]
cnt = 0
while cnt < 101:
    n_row = len(board)
    n_col = len(board[0])
    if c <= n_col and r <= n_row and board[r - 1][c - 1] == k:
        break

    if n_col <= n_row:  # R_sort
        elements = [0] * n_row
        cnt_element = 0  # set 중에 최대 길이

        for i in range(n_row):
            set_row = set(board[i]) - {0}
            elements[i] = set_row
            if cnt_element < len(set_row):
                cnt_element = len(set_row)

        n_col = cnt_element * 2
        new_board = [[0] * n_col for _ in range(n_row)]

        for i in range(n_row):
            tuple_row = []
            for j in range(len(elements[i])):
                a = elements[i].pop()
                b = board[i].count(a)
                tuple_row.append((b, a))
            tuple_row.sort()
            # print(tuple_row)
            for j in range(len(tuple_row[:50])):
                b, a = tuple_row[j]
                new_board[i][2 * j], new_board[i][2 * j + 1] = a, b

        board = [row[:] for row in new_board]

    else:
        board2 = list(map(list, zip(*board)))
        elements = [0] * n_col
        cnt_element = 0  # set 중에 최대 길이

        for i in range(n_col):
            set_row = set(board2[i]) - {0}
            elements[i] = set_row
            if cnt_element < len(set_row):
                cnt_element = len(set_row)

        n_row = cnt_element * 2
        new_board = [[0] * n_row for _ in range(n_col)]

        for i in range(n_col):
            tuple_row = []
            for j in range(len(elements[i])):
                a = elements[i].pop()
                b = board2[i].count(a)
                tuple_row.append((b, a))
            tuple_row.sort()

            for j in range(len(tuple_row[:50])):
                b, a = tuple_row[j]
                new_board[i][2 * j], new_board[i][2 * j + 1] = a, b
        board = list(map(list, zip(*new_board)))

    cnt += 1
if cnt == 101:
    print(-1)
else:
    print(cnt)
