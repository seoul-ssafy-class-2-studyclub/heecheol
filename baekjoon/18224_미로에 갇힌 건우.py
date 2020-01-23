import sys
# sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solution(idx1, idx2, cnt, is_sun):
    global shortcut
    global answer

    if cnt >= shortcut:
        return
    if idx1 == idx2 == N - 1:
        shortcut = cnt
        if is_sun == 1:
            answer = 'sun'
        else:
            answer = 'moon'
        return

    will_sun = is_sun
    for adj in adj_list:
        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if visit[nxt1][nxt2] is True:
                continue
            if board[nxt1][nxt2] == 0:
                visit[nxt1][nxt2] = True
                if cnt % M == 0:
                    will_sun = -(is_sun - 1)
                solution(nxt1, nxt2, cnt + 1, will_sun)
                visit[nxt1][nxt2] = False
            else:
                if is_sun == 0:
                    while True:
                        nxt1 += adj[0]
                        nxt2 += adj[1]
                        if 0 <= nxt1 < N and 0 <= nxt2 < N:
                            if board[nxt1][nxt2] == 1:
                                continue
                            else:
                                if visit[nxt1][nxt2] is True:
                                    break
                                else:
                                    visit[nxt1][nxt2] = True
                                    if cnt % M == 0:
                                        will_sun = -(is_sun - 1)
                                    solution(nxt1, nxt2, cnt + 1, will_sun)
                                    visit[nxt1][nxt2] = False
                                    break
                        else:
                            break


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

adj_list = [(0, -1), (-1, 0), (0, 1), (1, 0)]
visit = [[False] * N for _ in range(N)]
visit[0][0] = True

shortcut = float('inf')
answer = 0
solution(0, 0, 1, 1)    # idx1, idx2, cnt, is_sun

if answer == 0:
    print(-1)
else:
    if shortcut % (2 * M) == 0:
        day = shortcut // (2 * M)
    else:
        day = (shortcut // (2 * M)) + 1
    print(day, answer)
