import sys
sys.stdin = open('input.txt', 'r')


# 얼마나 녹을지 board2 생성
def step1():
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                cnt = 0
                for adj in adj_list:
                    nxt1, nxt2 = i + adj[0], j + adj[1]
                    if 0 <= nxt1 < N and 0 <= nxt2 < M:
                        if board[nxt1][nxt2] == 0:
                            cnt += 1
                board2[i][j] = cnt


# 녹이기 board - board2
def step2():
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                board[i][j] = board[i][j] - board2[i][j]
                if board[i][j] < 0:
                    board[i][j] = 0


# 분리되었는지 확인하기
def step3():
    board3 = [row[:] for row in board]
    count = 0
    for i in range(N):
        for j in range(M):
            if board3[i][j] != 0:
                count += 1
                queue = [(i, j)]
                while queue:
                    idx1, idx2 = queue.pop(0)
                    if board3[idx1][idx2] != 0:
                        board3[idx1][idx2] = 0
                        for adj in adj_list:
                            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                            if 0 <= nxt1 < N and 0 <= nxt2 < M:
                                if board3[nxt1][nxt2] != 0:
                                    queue.append((nxt1, nxt2))
    return count


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
year = 0
while True:
    year += 1
    board2 = [[0] * M for _ in range(N)]
    step1()
    step2()
    part = step3()
    if part == 1:
        continue
    elif part >= 2:
        break
    elif part == 0:
        year = 0
        break
print(year)


