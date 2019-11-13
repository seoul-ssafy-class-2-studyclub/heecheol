from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')


def bfs_up(ii):
    visit = [False] * N
    queue = collections.deque([ii])
    cnt = 0
    while queue:
        idx = queue.popleft()
        if visit[idx] is False:
            cnt += 1
            visit[idx] = True
            queue += taller[idx]
    return cnt


def bfs_down(ii):
    visit = [False] * N
    queue = collections.deque([ii])
    cnt = 0
    while queue:
        idx = queue.popleft()
        if visit[idx] is False:
            cnt += 1
            visit[idx] = True
            queue += shorter[idx]
    return cnt


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())

    taller = [[] for _ in range(N)]
    shorter = [[] for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        taller[a - 1].append(b - 1)
        shorter[b - 1].append(a - 1)

    result = []
    for i in range(N):
        result.append(bfs_up(i) + bfs_down(i) - 1)

    print('#{} {}'.format(tc, result.count(N)))

