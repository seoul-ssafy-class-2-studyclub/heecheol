import sys
sys.stdin = open('input.txt', 'r')


def numbering(idx1, idx2, num):
    board[idx1][idx2] = num

    for adj in adj_list:
        nxt1 = idx1 + adj[0]
        nxt2 = idx2 + adj[1]
        if board[nxt1][nxt2] == '#':
            numbering(nxt1, nxt2, num)


def route(idx1, idx2, s):
    global flag1
    if len(routes[s]) >= 2:
        flag1 = False
        return

    elif board[idx1][idx2] == '0':
        # print(routes)
        routes[s].add(''.join(arr))
        print(routes[s])
        print('#1', arr)
        arr.pop()
        if len(arr) == 1:
            safe.add(s)
            routes[s] += 1
            flag1 = False
            return
        else:
            return
    #
    # elif board[idx1][idx2] in safe:
    #     routes[s] += 1
    #     print('#2', arr)
    #     # print(routes)
    #     return

    else:
        for adj in adj_list:
            nxt1 = idx1 + adj[0]
            nxt2 = idx2 + adj[1]
            if visit[nxt1][nxt2] is False:
                visit[nxt1][nxt2] = True
                if board[nxt1][nxt2] == '.':
                    route(nxt1, nxt2, s)
                elif board[nxt1][nxt2] not in arr:
                    arr.append(board[nxt1][nxt2])
                    route(nxt1, nxt2, s)
                if flag1 is False:
                    break
                visit[nxt1][nxt2] = False


N, M = map(int, input().split())

board = [list(input()) for _ in range(N)]
board2 = [['.'] * M for _ in range(N)]

safe = set()

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# edge to zero
for i in range(N):
    for j in range(M):
        if i == 0 or i == N -1 or j == 0 or j == M -1:
            board[i][j] = '0'

# 섬 구분하기 from 1
n = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == '#':
            n += 1
            numbering(i, j, str(n))
routes = [set() for _ in range(n + 1)]

# 1번 섬부터 안전한지 체크
m = 5
flag = True
flag1 = True
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == str(m):
            visit = [[False] * M for _ in range(N)]
            arr = [str(m)]
            route(i, j, m)
            m += 1
            if m > n:
                flag = False
                break
    if flag is False:
        break
print(routes)