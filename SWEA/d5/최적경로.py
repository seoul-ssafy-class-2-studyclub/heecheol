import sys
sys.stdin = open('input.txt', 'r')


def grid_distance(distance, cnt, pre=0):
    if cnt == N:
        x, y = arr[1]
        px, py = arr[pre]
        dd = abs(x - px) + abs(y - py)
        return distance + dd

    else:
        px, py = arr[pre]
        grid_min = float('inf')
        for i in range(2, N + 2):
            if grid_visit[i] is False:
                x, y = arr[i]
                dd = abs(x - px) + abs(y - py)
                if grid_min > dd:
                    grid_min = dd
                    nxt = i
        grid_visit[nxt] = True
        return grid_distance(distance+grid_min, cnt+1, nxt)


def mydef(distance, cnt, pre=0):
    global min_distance
    if distance >= min_distance:
        return

    elif cnt == N:
        x, y = arr[1]
        px, py = arr[pre]
        dd = abs(x - px) + abs(y - py)
        if min_distance > distance + dd:
            min_distance = distance + dd
            return

    else:
        for i in range(2, N + 2):
            if visit[i] is False:
                visit[i] = True
                x, y = arr[i]
                px, py = arr[pre]
                dd = abs(x - px) + abs(y - py)
                mydef(distance + dd, cnt + 1, i)
                visit[i] = False


for tc in range(1, int(input()) + 1):
    N = int(input())
    data = list(map(int, input().split()))

    arr = [0] * (N+2)
    for n in range(N+2):
        arr[n] = (data[2*n], data[2*n + 1])

    grid_visit = [False] * (N + 2)

    visit = [False] * (N + 2)
    min_distance = float('inf')
    min_distance = grid_distance(0, 0)
    mydef(0, 0)
    print('#{} {}'.format(tc, min_distance))