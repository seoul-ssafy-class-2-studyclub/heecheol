import sys
sys.stdin = open('input.txt', 'r')


def board_init():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        board[a - 1][b - 1] = 1
    board[0][0] = 2


def eat_apple(idx1, idx2):
    snake.append((idx1, idx2))
    board[idx1][idx2] = 2


def no_apple(idx1, idx2):
    snake.append((idx1, idx2))
    board[idx1][idx2] = 2
    tail = snake.pop(0)
    board[tail[0]][tail[1]] = 0


N = int(input())
board = [[0] * N for _ in range(N)]
board_init()

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

snake = [(0, 0)]
current_direction = 1
current_time = 0

blocked = False
for _ in range(int(input())):
    str_time, next_direction = input().split()
    time_to_turn = int(str_time)

    while current_time < time_to_turn:
        current_time += 1
        head_idx1, head_idx2 = snake[-1]

        nxt1, nxt2 = head_idx1 + adj_list[current_direction][0], head_idx2 + adj_list[current_direction][1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if board[nxt1][nxt2] == 0:
                no_apple(nxt1, nxt2)

            elif board[nxt1][nxt2] == 1:
                eat_apple(nxt1, nxt2)

            else:
                # blocked by snake's body
                blocked = True
                break

        else:
            # blocked by wall
            blocked = True
            break

    if blocked:
        break

    else:
        if next_direction == 'L':
            current_direction = (current_direction - 1) % 4
        else:
            current_direction = (current_direction + 1) % 4

if blocked:
    print(current_time)

else:
    while True:
        current_time += 1
        head_idx1, head_idx2 = snake[-1]

        nxt1, nxt2 = head_idx1 + adj_list[current_direction][0], head_idx2 + adj_list[current_direction][1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if board[nxt1][nxt2] == 0:
                no_apple(nxt1, nxt2)

            elif board[nxt1][nxt2] == 1:
                eat_apple(nxt1, nxt2)

            else:
                # blocked by snake's body
                blocked = True
                break

        else:
            # blocked by wall
            blocked = True
            break

    print(current_time)
