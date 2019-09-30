import sys
sys.stdin = open('input.txt', 'r')


def chk(ix, iy, arr, cnt):
    if cnt == 7:
        result.add(''.join(arr))
        return
    else:
        for nxt in adj_list:
            nx, ny = ix + nxt[0], iy + nxt[1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                arr.append(board[nx][ny])
                chk(nx, ny, arr, cnt+1)
                arr.pop()


for tc in range(1, int(input()) + 1):
    board = [input().split() for _ in range(4)]

    result = set()
    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for i in range(4):
        for j in range(4):
            arr = []
            chk(i, j, arr, 0)

    print('#{} {}'.format(tc, len(result)))