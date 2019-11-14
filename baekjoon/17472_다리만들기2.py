import heapq
from pprint import pprint
import collections
import sys
sys.stdin = open('input.txt', 'r')


# step1
def assortment():
    mark = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == '1':
                mark += 1
                queue = collections.deque([(i, j)])
                while queue:
                    idx1, idx2 = queue.popleft()
                    if board[idx1][idx2] == '1':
                        board[idx1][idx2] = mark
                        for adj in adj_list:
                            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                                if board[nxt1][nxt2] == '1':
                                    queue.append((nxt1, nxt2))

            # 보기편하게, 나중에 수정하기
            elif board[i][j] == '0':
                board[i][j] = 0
            # 이거 지우고 0 바꾸기
    return mark


def route():
    for row in range(N):
        col = 0
        while col < M:
            if board[row][col] != 0:
                s = board[row][col]
                col += 1
                cnt = 0
                while col < M:
                    if board[row][col] == 0:
                        cnt += 1
                        col += 1
                    elif board[row][col] == s:
                        col += 1
                        cnt = 0
                        continue
                    else:
                        if cnt <= 1:
                            break
                        else:
                            e = board[row][col]
                            if distance[s][e][0] > cnt:
                                distance[s][e] = (cnt, s, e)
                                distance[e][s] = (cnt, e, s)
                            break
            else:
                col += 1
    for col in range(M):
        row = 0
        while row < N:
            if board[row][col] != 0:
                s = board[row][col]
                row += 1
                cnt = 0
                while row < N:
                    if board[row][col] == 0:
                        cnt += 1
                        row += 1
                    elif board[row][col] == s:
                        cnt = 0
                        row += 1
                        continue
                    else:
                        if cnt <= 1:
                            break
                        else:
                            e = board[row][col]
                            if distance[s][e][0] > cnt:
                                distance[s][e] = (cnt, s, e)
                                distance[e][s] = (cnt, e, s)
                            break
            else:
                row += 1


N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

K = assortment()

inf = float('inf')
distance = [[(inf, k, k)] * (K + 1) for k in range(K + 1)]

# step2 => 섬 사이의 거리
route()


connected = [1]
arr = []
for i in range(1, K + 1):
    heapq.heappush(arr, distance[1][i])
result = 0
flag = True
while arr:
    if len(connected) >= K:
        break
    d, s_node, e_node = heapq.heappop(arr)
    # print()

    if d == inf:
        flag = False
        break

    if e_node in connected:
        continue

    else:
        result += d
        for i in range(1, K + 1):
            heapq.heappush(arr, distance[e_node][i])
        connected.append(e_node)

# pprint(board)
# for row in range(1, K + 1):
#     print(distance[row][1:])

if flag is True:
    print(result)
else:
    print(-1)
