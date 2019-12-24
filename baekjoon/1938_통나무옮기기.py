from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [list(input()) for _ in range(N)]

tree = []
end = []
end_status = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == '0' or board[i][j] == '1':
            continue
        if board[i][j] == 'B':
            tree.append((i, j))
        else:
            end.append((i, j))

# 0, 1, 2, 3
visit = [[0] * N for _ in range(N)]

if tree[0][0] == tree[1][0]:    # 가로는 1
    visit[tree[0][0]][tree[0][1]] = 1
else:
    visit[tree[0][0]][tree[0][1]] = 2

if end[0][0] == end[1][0]:
    end_status = 1
else:
    end_status = 2

# pprint(visit)
# 위 - 오른쪽 - 아래 - 왼쪽 순
adj_two = [[(-1, 0)], [(0, 1), (1, 1), (2, 1)], [(1, 0), (3, 0)], [(0, -1), (1, -1), (2, -1)]]
adj_one = [[(-1, 0), (-1, 1), (-1, 2)], [(0, 1), (0, 3)], [(1, 0), (1, 1), (1, 2)], [(0, -1)]]
turn_two_one = [(0, -1), (0, 1), (1, -1), (1, 1), (2, -1), (2, 1)]
turn_one_two = [(-1, 0), (-1, 1), (-1, 2), (1, 0), (1, 1), (1, 2)]

queue = [(tree[0][0], tree[0][1], visit[tree[0][0]][tree[0][1]], 0)]
result = 0
while queue:
    # print(queue)
    for _ in range(len(queue)):
        idx1, idx2, status, cnt = queue.pop(0)
        if idx1 == end[0][0] and idx2 == end[0][1] and end_status == status:
            result = cnt
            queue = False
            break

        if status == 2:
            for adj_list in adj_two:
                n1, n2 = idx1 + adj_list[0][0], idx2 + adj_list[0][1]

                if 0 <= n1 < N and 0 <= n2 < N and visit[n1][n2] < 2:
                    flag = True
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < N and 0 <= nxt2 < N:
                            if board[nxt1][nxt2] == '1':
                                flag = False
                                break
                        else:
                            flag = False
                            break

                    if flag is True:
                        visit[n1][n2] += 2
                        queue.append((n1, n2, 2, cnt + 1))

            flag = True
            for adj in turn_two_one:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]

                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if board[nxt1][nxt2] == '1':
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag is True:
                n1, n2 = idx1 + 1, idx2 - 1
                if visit[n1][n2] % 2 is 0:
                    visit[n1][n2] += 1
                    queue.append((n1, n2, 1, cnt + 1))

        elif status == 1:
            for adj_list in adj_one:
                n1, n2 = idx1 + adj_list[0][0], idx2 + adj_list[0][1]

                if 0 <= n1 < N and 0 <= n2 < N and visit[n1][n2] % 2 is 0:
                    flag = True
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < N and 0 <= nxt2 < N:
                            if board[nxt1][nxt2] == '1':
                                flag = False
                                break
                        else:
                            flag = False
                            break

                    if flag is True:
                        visit[n1][n2] += 1
                        queue.append((n1, n2, 1, cnt + 1))

            flag = True
            for adj in turn_one_two:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]

                if 0 <= nxt1 < N and 0 <= nxt2 < N:
                    if board[nxt1][nxt2] == '1':
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag is True:
                n1, n2 = idx1 - 1, idx2 + 1
                if visit[n1][n2] < 2:
                    visit[n1][n2] += 2
                    queue.append((n1, n2, 2, cnt + 1))

print(result)
