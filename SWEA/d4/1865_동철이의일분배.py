#
# ################################ ver.1
# # import sys
# # sys.stdin = open("input.txt", "r")
#
#
# def solve(k):
#     global ans
#     if k == N :
#         val = 1
#         for i in range(N):
#             val *= mat[i][perm[i]]
#         if val > ans:
#             ans = val
#     else:
#         for i in range(k, N):
#             perm[k], perm[i] = perm[i], perm[k]
#             solve(k + 1)
#             perm[k], perm[i] = perm[i], perm[k]
#
#
# TC = int(input())
# for tc in range(1, TC + 1):
#     N = int(input())
#
#     mat = [0.0] * N
#     for i in range(N):
#         mat[i] = list(map(lambda x: int(x)/100, input().split()))
#
#     ans = 0
#     perm = [x for x in range(N)]
#     solve(0)
#     print("#%d %.6f" % (tc, ans * 100))
#



#
# ################################ ver.2
# # import sys
# # import time
# # sys.stdin = open("input.txt", "r")
# #
# # st = time.time()
#
# def solve(k):
#     global ans
#     global cnt
#     cnt += 1
#     if k == N :
#         val = 1
#         for i in range(N):
#             val *= mat[i][perm[i]]
#         if val > ans:
#             ans = val
#     else:
#         for i in range(k, N):
#             perm[k], perm[i] = perm[i], perm[k]
#             val = 1
#             for j in range(k + 1):
#                 val *= mat[j][perm[j]]
#             if val > ans:
#                 solve(k + 1)
#             perm[k], perm[i] = perm[i], perm[k]
#
#
#
# for tc in range(1, int(input()) + 1):
#     N = int(input())
#
#     mat = [0.0] * N
#     for i in range(N):
#         mat[i] = list(map(lambda x: int(x) / 100, input().split()))
#
#     cnt = 0
#     ans = 0
#     perm = [x for x in range(N)]
#     solve(0)
#     print("#%d %.6f" % (tc, ans * 100))
#
# #     print("#%d %.6f" % (tc, ans * 100), cnt)
# #
# # print(time.time() - st)
#





# ################################ ver.3
import sys
# import time
sys.stdin = open("input.txt", "r")
#
# st = time.time()


def grid_ans():
    global ans
    val = 1
    chk = [0] * N
    for i in range(N):
        tmaxi = 0
        for j in range(N):
            if not chk[j] and tmaxi < mat[i][j]:
                tmaxi = j
        chk[tmaxi] = 1
        val *= mat[i][tmaxi]
    ans = val


def solve(k, val):
    global ans
    global cnt
    cnt += 1
    if k == N:
        if val > ans:
            ans = val
    else:
        for i in range(k, N):
            perm[k], perm[i] = perm[i], perm[k]
            if val * mat[k][perm[k]] > ans:
                solve(k + 1, val * mat[k][perm[k]])
            perm[k], perm[i] = perm[i], perm[k]


for tc in range(1, int(input()) + 1):
    N = int(input())

    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(lambda x: int(x)/100, input().split()))

    cnt = 0
    ans = 0
    perm = [x for x in range(N)]

    grid_ans()

    solve(0, 1)
    print("#%d %.6f" % (tc, ans * 100))
    # print("#%d %.6f" % (tc, ans * 100), cnt)

# print(time.time() - st)

