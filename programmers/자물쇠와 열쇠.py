from pprint import pprint


def solution(key, lock):
    N = len(key)
    M = len(lock)

    # key 회전
    # key_90 = [[0] * N for _ in range(N)]
    # key_180 = [[0] * N for _ in range(N)]
    # key_270 = [[0] * N for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    #         key_90[i][j] = key[N - j - 1][i]
    #         key_270[i][j] = key[j][N - i - 1]
    #         key_180[i][j] = key[N - i - 1][N - j - 1]

    board = [[0] * (N + M - 1) for _ in range(N + M - 1)]
    for i in range(M):
        for j in range(M):
            board[N + i - 1][N + j - 1] = lock[i][j]

    answer = False

    for si in range(N + M - 1):
        for sj in range(N + M - 1):
            flag0 = flag90 = flag180 = flag270 = True
            # print(si, sj)
            for r in range(M - 1, M + N - 1):
                for c in range(M - 1, M + N - 1):
                    print(si, sj, r, c)
                    print(r - M + si + 1, c - M + sj + 1)
                    if flag0 is True:
                        if board[r][c] == 0:
                            if r + si > M + N - 2 or c + sj > M + N - 2:
                                flag0 = False
                            elif key[r + si][c + sj] == 0:
                                flag0 = False
                        else:
                            if r > si + M - 1 or c > sj + M - 1:
                                pass
                            if key[r - M + si + 1][c - M + sj + 1] == 1:
                                flag0 = False
                    # if flag90 is True:
                    #     if board[r][c] == 0:
                    #         if r + si > M + N - 2 or c + sj > M + N - 2:
                    #             flag90 = False
                    #         elif key_90[r + si][c + sj] == 0:
                    #             flag90 = False
                    #     else:
                    #         if r > si + M - 1 or c > sj + M - 1:
                    #             pass
                    #         if key_90[r - M + si][c - M + sj] == 1:
                    #             flag90 = False
                    # if flag180 is True:
                    #     if board[r][c] == 0:
                    #         if r + si > M + N - 2 or c + sj > M + N - 2:
                    #             flag0 = False
                    #         elif key_180[r + si][c + sj] == 0:
                    #             flag180 = False
                    #     else:
                    #         if r > si + M - 1 or c > sj + M - 1:
                    #             pass
                    #         if key_180[r - M + si][c - M + sj] == 1:
                    #             flag180 = False
                    # if flag270 is True:
                    #     if board[r][c] == 0:
                    #         if r + si > M + N - 2 or c + sj > M + N - 2:
                    #             flag270 = False
                    #         elif key_270[r + si][c + sj] == 0:
                    #             flag270 = False
                    #     else:
                    #         if r > si + M - 1 or c > sj + M - 1:
                    #             pass
                    #         if key_270[r - M + si][c - M + sj] == 1:
                    #             flag270 = False
            # if flag0 or flag90 or flag180 or flag270:
            if flag0:
                answer = True
                break
        if answer is True:
            break

    return answer


# input_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
input_key = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
input_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(input_key, input_lock)
