import sys
sys.stdin = open('input.txt', 'r')
import heapq


def init():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0
                return [i, j]


def find_target():
    for i in range(N):
        for j in range(N):
            if 0 < board[i][j] < size:
                return True
    return False


def find_path():
    if not find_target():
        return [0, 0, 0]

    visit = [[False] * N for _ in range(N)]
    visit[shark[0]][shark[1]] = True

    queue = [(shark[0], shark[1])]
    second = 0
    heap = []
    while queue:
        second += 1
        for _ in range(len(queue)):
            idx1, idx2 = queue.pop(0)
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if not visit[nxt1][nxt2]:
                        if 0 < board[nxt1][nxt2] < size:
                            visit[nxt1][nxt2] = True
                            heapq.heappush(heap, [second, nxt1, nxt2])
                        elif board[nxt1][nxt2] <= size:
                            visit[nxt1][nxt2] = True
                            queue.append((nxt1, nxt2))
        if heap:
            return heapq.heappop(heap)

    return [0, 0, 0]


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

shark = init()
size = 2

adj_list = [(-1, 0), (0, -1), (0, 1), (1, 0)]
result = 0
ate = 0

while True:
    res = find_path()
    if res[0] == 0:
        break

    result += res[0]
    board[res[1]][res[2]] = 0

    ate += 1
    if ate == size:
        size += 1
        ate = 0

    shark = [res[1], res[2]]

print(result)

