from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

def tunnel(row, col, cnt):
    visited[row][col] = True
    visited2[row][col] = True
    # print(row, col,'-' , cnt)

    if cnt == L:
        pass
        # print('--')
    else:
        idx = board[row][col]
        # 각 타입별 예외 처리
        if idx == 1:
            for i in range(4):
                nxt1 = row + adj_list[1][i][0]
                nxt2 = col + adj_list[1][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:      # (0, -1) 왼쪽
                        if board[nxt1][nxt2] not in left_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:    # (-1, 0) 위쪽
                        if board[nxt1][nxt2] not in up_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 2:    # 오른쪽
                        if board[nxt1][nxt2] not in right_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 3:  # 아래
                        if board[nxt1][nxt2] not in down_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
        elif idx == 2:
            for i in range(2):
                nxt1 = row + adj_list[2][i][0]
                nxt2 = col + adj_list[2][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:  # (-1, 0) 위쪽
                        if board[nxt1][nxt2] not in up_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:  # (1, 0) 아래쪽
                        if board[nxt1][nxt2] not in down_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
        elif idx == 3:
            for i in range(2):
                nxt1 = row + adj_list[3][i][0]
                nxt2 = col + adj_list[3][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:  # (0, -1) 왼쪽
                        if board[nxt1][nxt2] not in left_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:  # (0, 1)
                        if board[nxt1][nxt2] not in right_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
        elif idx == 4:
            for i in range(2):
                nxt1 = row + adj_list[4][i][0]
                nxt2 = col + adj_list[4][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:  # (-1, 0) 위
                        if board[nxt1][nxt2] not in up_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:  # (0, 1) 오른쪽
                        if board[nxt1][nxt2] not in right_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False

        elif idx == 5:
            for i in range(2):
                nxt1 = row + adj_list[5][i][0]
                nxt2 = col + adj_list[5][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:  # (0, 1) 오른쪽
                        if board[nxt1][nxt2] not in right_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:  # (1, 0) 아래쪽
                        if board[nxt1][nxt2] not in down_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
        elif idx == 6:
            for i in range(2):
                nxt1 = row + adj_list[6][i][0]
                nxt2 = col + adj_list[6][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:  # (0, -1) 왼쪽
                        if board[nxt1][nxt2] not in left_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:  # (1, 0) 아래쪽
                        if board[nxt1][nxt2] not in down_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
        elif idx == 7:
            for i in range(2):
                nxt1 = row + adj_list[7][i][0]
                nxt2 = col + adj_list[7][i][1]
                if 0 <= nxt1 < N and 0 <= nxt2 < M:
                    if i == 0:  # (0, -1) 왼쪽
                        if board[nxt1][nxt2] not in left_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False
                    elif i == 1:  # (-1, 0) 위쪽
                        if board[nxt1][nxt2] not in up_except and visited[nxt1][nxt2] is False:
                            tunnel(nxt1, nxt2, cnt + 1)
                            visited[nxt1][nxt2] = False


for tc in range(1, int(input())+1):
    N, M, R, C, L = map(int, input().split())
    # N: 세로, M: 가로, R, C: 맨홀위치, L: 탈출 후 시간

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]     # 나중에 True 갯수 체크하면 끝
    visited2 = [[False] * M for _ in range(N)]
    adj_list = [[], [[0, -1], [-1, 0], [0, 1], [1, 0]], [[-1, 0], [1, 0]], [[0, -1], [0, 1]], [[-1, 0], [0, 1]],
                [[0, 1], [1, 0]], [[0, -1], [1, 0]], [[0, -1], [-1, 0]]]

    left_except = [0, 2, 6, 7]
    up_except = [0, 3, 4, 7]
    right_except = [0, 2, 4, 5]
    down_except = [0, 3, 5, 6]

    tunnel(R, C, 1)

    count = 0
    for i in range(N):
        for j in range(M):
            if visited2[i][j] is True:
                count += 1

    print('#{} {}'.format(tc, count))
