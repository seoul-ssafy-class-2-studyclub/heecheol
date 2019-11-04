from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
board2 = [[[] for _ in range(N)] for _ in range(N)]

# pieces, dirs index from 0
pieces = [0] * K

for i in range(K):
    r, c, d = map(int, input().split())
    pieces[i] = [r - 1, c - 1, d - 1]
    board2[r - 1][c - 1].append(i)

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
flag = True
cnt = 0
while cnt < 1000:
    cnt += 1

    for i in range(K):  # 모든 i 에 대해서 move
        r, c, d = pieces[i]

        nxt1, nxt2 = r + dirs[pieces[i][2]][0], c + dirs[pieces[i][2]][1]
        idx = board2[r][c].index(i)  # idx 는 i 의 인덱스
        arr = board2[r][c][idx:]

        if 0 <= nxt1 < N and 0 <= nxt2 < N:

            if board[nxt1][nxt2] == 0:
                for _ in range(len(arr)):    # idx 부터
                    p = board2[r][c].pop(idx)
                    board2[nxt1][nxt2].append(p)
                    pieces[p][0], pieces[p][1] = nxt1, nxt2

            elif board[nxt1][nxt2] == 1:
                for _ in range(len(arr)):
                    p = board2[r][c].pop()
                    board2[nxt1][nxt2].append(p)
                    pieces[p][0], pieces[p][1] = nxt1, nxt2

            else:
                nxt1, nxt2 = r - dirs[pieces[i][2]][0], c - dirs[pieces[i][2]][1]
                pieces[i][2] ^= 1
                if nxt1 < 0 or nxt1 >= N or nxt2 < 0 or nxt2 >= N or board[nxt1][nxt2] == 2:
                    continue

                elif board[nxt1][nxt2] == 0:
                    for _ in range(len(arr)):
                        p = board2[r][c].pop(idx)
                        board2[nxt1][nxt2].append(p)
                        pieces[p][0], pieces[p][1] = nxt1, nxt2

                elif board[nxt1][nxt2] == 1:
                    for _ in range(len(arr)):
                        p = board2[r][c].pop()
                        board2[nxt1][nxt2].append(p)
                        pieces[p][0], pieces[p][1] = nxt1, nxt2

        else:
            nxt1, nxt2 = r - dirs[pieces[i][2]][0], c - dirs[pieces[i][2]][1]
            pieces[i][2] ^= 1

            if board[nxt1][nxt2] == 2:
                continue

            elif board[nxt1][nxt2] == 1:
                for _ in range(len(arr)):
                    p = board2[r][c].pop()
                    board2[nxt1][nxt2].append(p)
                    pieces[p][0], pieces[p][1] = nxt1, nxt2

            else:
                for _ in range(len(arr)):
                    p = board2[r][c].pop(idx)
                    board2[nxt1][nxt2].append(p)
                    pieces[p][0], pieces[p][1] = nxt1, nxt2

        if len(board2[nxt1][nxt2]) >= 4:
            flag = False
            break

    if flag is False:
        break

if flag is False:
    print(cnt)
else:
    print(-1)
