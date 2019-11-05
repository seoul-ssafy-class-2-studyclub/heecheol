from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
board = [list(input().split()) for _ in range(N)]
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
    for i in range(K):
        pprint(board2)
        print()
        r, c, d = pieces[i]
        # can move
        if board2[r][c][0] == i:
            # one piece
            if len(board2[r][c]) == 1:
                nxt1, nxt2 = r + dirs[pieces[i][2]][0], c + dirs[pieces[i][2]][1]
                # 하나, 막혀있음
                if nxt1 < 0 or nxt1 >= N or nxt2 < 0 or nxt2 >= N or board[nxt1][nxt2] == 2:
                    nxt1, nxt2 = r - dirs[pieces[i][2]][0], c - dirs[pieces[i][2]][1]

                    if board[nxt1][nxt2] == 2:
                        pieces[i][2] = (pieces[i][2] + 2) % 4

                    else:
                        pieces[i][0], pieces[i][1] = nxt1, nxt2
                        pieces[i][2] = (pieces[i][2] + 2) % 4
                        board2[nxt1][nxt2].append(board2[r][c].pop())

                else:
                    pieces[i][0], pieces[i][1] = nxt1, nxt2
                    board2[nxt1][nxt2].append(board2[r][c].pop())

            # more than one piece
            else:
                nxt1, nxt2 = r + dirs[pieces[i][2]][0], c + dirs[pieces[i][2]][1]

                if nxt1 < 0 or nxt1 >= N or nxt2 < 0 or nxt2 >= N or board[nxt1][nxt2] == 2:
                    nxt1, nxt2 = r - dirs[pieces[i][2]][0], c - dirs[pieces[i][2]][1]

                    if board[nxt1][nxt2] == 2:
                        pieces[i][2] = (pieces[i][2] + 2) % 4

                    elif board[nxt1][nxt2] == 1:
                        for _ in range(len(board2[r][c])):
                            p = board2[r][c].pop()
                            board2[nxt1][nxt2].append(p)
                            pieces[p][0], pieces[p][1] = nxt1, nxt2
                        pieces[i][2] = (pieces[i][2] + 2) % 4

                    else:
                        for _ in range(len(board2[r][c])):
                            p = board2[r][c].pop(0)
                            board2[nxt1][nxt2].append(p)
                            pieces[p][0], pieces[p][1] = nxt1, nxt2
                        pieces[i][2] = (pieces[i][2] + 2) % 4

                elif board[nxt1][nxt2] == 1:
                    for _ in range(len(board2[r][c])):
                        p = board2[r][c].pop()
                        board2[nxt1][nxt2].append(p)
                        pieces[p][0], pieces[p][1] = nxt1, nxt2

                else:
                    for _ in range(len(board2[r][c])):
                        p = board2[r][c].pop(0)
                        board2[nxt1][nxt2].append(p)
                        pieces[p][0], pieces[p][1] = nxt1, nxt2

    if len(board2[nxt1][nxt2]) >= 4:
        pprint(board2)
        flag = False
        break
    #
    # if flag is False:
    #     break

if flag is False:
    print(cnt)
else:
    print(-1)