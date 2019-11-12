import sys
sys.stdin = open('input.txt', 'r')


def step1():
    queue = [(0, 0)]

    while queue:
        idx1, idx2 = queue.pop(0)
        if board[idx1][idx2] == 0:
            board[idx1][idx2] = 2
            for adj in adj_list:
                nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                if 0 <= nxt1 < R and 0 <= nxt2 < C:
                    if board[nxt1][nxt2] == 0:
                        queue.append((nxt1, nxt2))


def step2():
    for i in range(R):
        for j in range(C):
            if board[i][j] == 1:
                for adj in adj_list:
                    nxt1, nxt2 = i + adj[0], j + adj[1]
                    if 0 <= nxt1 < R and 0 <= nxt2 < C and board[nxt1][nxt2] == 2:
                        board[i][j] = 3
                        break


def step3():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == 3:
                board[i][j] = 0
                cnt += 1
            elif board[i][j] == 2:
                board[i][j] = 0
    return cnt


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
t = 0
cnt_list = []
while True:
    step1()
    step2()
    cnt_list.append(step3())
    if cnt_list[-1] == 0:
        break
    t += 1

print(t)
print(cnt_list[-2])
