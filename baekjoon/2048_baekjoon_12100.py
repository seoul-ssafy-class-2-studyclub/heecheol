import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
board_origin = [list(map(int, input().split())) for _ in range(N)]


def push_left():
    global max_num

    changed = False

    for row in range(N):
        for i in range(N-1):
            if board_left[row][i] == 0:
                continue
            else:
                for j in range(i+1, N):
                    if board_left[row][j] == 0:
                        continue
                    elif board_left[row][j] == board_left[row][i]:
                        board_left[row][i] *= 2
                        board_left[row][j] = 0
                        changed = True
                        break
                    else:
                        break

    for row in range(N):
        for i in range(N-1):
            if board_left[row][i] == 0:
                for j in range(i+1, N):
                    if board_left[row][j] == 0:
                        continue
                    else:
                        board_left[row][i], board_left[row][j] = board_left[row][j], board_left[row][i]
                        changed = True
                        break

    cnt = 0
    for row in range(N):
        for col in range(N):
            if board_left[row][col] == 0:
                continue
            else:
                cnt += 1
                if board_left[row][col] > max_num:
                    max_num = board_left[row][col]

    if cnt > 1:
        return False, changed
    else:
        return True, changed


def push_up():
    global max_num

    changed = False

    for col in range(N):
        for i in range(N - 1):
            if board_up[i][col] == 0:
                continue
            else:
                for j in range(i + 1, N):
                    if board_up[j][col] == 0:
                        continue
                    elif board_up[j][col] == board_up[i][col]:
                        board_up[i][col] *= 2
                        board_up[j][col] = 0
                        changed = True
                        break
                    else:
                        break

    for col in range(N):
        for i in range(N - 1):
            if board_up[i][col] == 0:
                for j in range(i + 1, N):
                    if board_up[j][col] == 0:
                        continue
                    else:
                        board_up[i][col], board_up[j][col] = board_up[j][col], board_up[i][col]
                        changed = True
                        break

    cnt = 0
    for row in range(N):
        for col in range(N):
            if board_up[row][col] == 0:
                continue
            else:
                cnt += 1
                if board_up[row][col] > max_num:
                    max_num = board_up[row][col]

    if cnt > 1:
        return False, changed
    else:
        return True, changed


def push_right():
    global max_num

    changed = False

    for row in range(N):
        for i in range(N - 1, 0, -1):
            if board_right[row][i] == 0:
                continue
            else:
                for j in range(i - 1, -1, -1):
                    if board_right[row][j] == 0:
                        continue
                    elif board_right[row][j] == board_right[row][i]:
                        board_right[row][i] *= 2
                        board_right[row][j] = 0
                        changed = True
                        break
                    else:
                        break

    for row in range(N):
        for i in range(N - 1, 0, -1):
            if board_right[row][i] == 0:
                for j in range(i - 1, -1, -1):
                    if board_right[row][j] == 0:
                        continue
                    else:
                        board_right[row][i], board_right[row][j] = board_right[row][j], board_right[row][i]
                        changed = True
                        break

    cnt = 0
    for row in range(N):
        for col in range(N):
            if board_right[row][col] == 0:
                continue
            else:
                cnt += 1
                if board_right[row][col] > max_num:
                    max_num = board_right[row][col]

    if cnt > 1:
        return False, changed
    else:
        return True, changed


def push_down():
    global max_num

    changed = False

    for col in range(N):
        for i in range(N - 1, 0, -1):
            if board_down[i][col] == 0:
                continue
            else:
                for j in range(i - 1, -1, -1):
                    if board_down[j][col] == 0:
                        continue
                    elif board_down[j][col] == board_down[i][col]:
                        board_down[i][col] *= 2
                        board_down[j][col] = 0
                        changed = True
                        break
                    else:
                        break

    for col in range(N):
        for i in range(N - 1, 0, -1):
            if board_down[i][col] == 0:
                for j in range(i - 1, -1, -1):
                    if board_down[j][col] == 0:
                        continue
                    else:
                        board_down[i][col], board_down[j][col] = board_down[j][col], board_down[i][col]
                        changed = True
                        break

    cnt = 0
    for row in range(N):
        for col in range(N):
            if board_down[row][col] == 0:
                continue
            else:
                cnt += 1
                if board_down[row][col] > max_num:
                    max_num = board_down[row][col]

    if cnt > 1:
        return False, changed
    else:
        return True, changed


queue = [board_origin]
max_num = 0

flag_finish = False
for __ in range(5):

    for _ in range(len(queue)):
        board_pop = queue.pop(0)

        board_left = [row[:] for row in board_pop]
        A, B = push_left()
        if B:
            queue.append(board_left)
        if A:
            flag_finish = True
            break

        board_right = [row[:] for row in board_pop]
        A, B = push_right()
        if B:
            queue.append(board_right)
        if A:
            flag_finish = True
            break

        board_up = [row[:] for row in board_pop]
        A, B = push_up()
        if B:
            queue.append(board_up)
        if A:
            flag_finish = True
            break

        board_down = [row[:] for row in board_pop]
        A, B = push_down()
        if B:
            queue.append(board_down)
        if A:
            flag_finish = True
            break

    if flag_finish:
        break

print(max_num)
