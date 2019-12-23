from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
board = [[0] * N for _ in range(N)]
board[0][0] = 2     # 뱀
D = [(-1, 0), (0, 1), (1, 0), (0, -1)]
di = 1

K = int(input())
for _ in range(K):
    a1, a2 = map(int, input().split())
    board[a1 - 1][a2 - 1] = 1   # 사과

time = 0
queue = [(0, 0)]

flag = True     # for what?
L = int(input())
xlist = []
clist = []
for _ in range(L):
    X, C = input().split()
    xlist.append(X)
    clist.append(C)

inf = 987654321
xlist.append(inf)
clist.append(inf)

for i in range(L + 1):
    X, C = xlist[i], clist[i]

    while True:
        # pprint(board)
        # print()
        time += 1
        idx1, idx2 = queue[-1]      # 뱀 머리
        nxt1, nxt2 = idx1 + D[di][0], idx2 + D[di][1]
        if 0 <= nxt1 < N and 0 <= nxt2 < N:
            if board[nxt1][nxt2] == 1:
                queue.append((nxt1, nxt2))
                board[nxt1][nxt2] = 2

            elif board[nxt1][nxt2] == 0:
                queue.append((nxt1, nxt2))
                tail1, tail2 = queue.pop(0)
                board[nxt1][nxt2] = 2
                board[tail1][tail2] = 0

            elif board[nxt1][nxt2] == 2:
                flag = False
                break
                # if nxt1 == queue[0][0] and nxt2 == queue[0][1]:
                #     queue.append((nxt1, nxt2))
                #     queue.pop(0)
                # else:
                #     flag = False
                #     break
        else:
            flag = False
            break

        if flag is False:
            break

        if time == int(X):
            if C == 'L':
                di = (di - 1) % 4
            elif C == 'D':
                di = (di + 1) % 4
            break

    if flag is False:
        break

print(time)
