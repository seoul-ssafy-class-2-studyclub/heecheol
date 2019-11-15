import sys
sys.stdin = open('input.txt', 'r')


def dfs(idx1, idx2, status):
    global cnt

    if idx1 == idx2 == N - 1:
        cnt += 1
        return

    else:
        if status == 0:
            if idx2 + 1 < N and board[idx1][idx2 + 1] == 0:
                dfs(idx1, idx2 + 1, 0)

                if idx1 + 1 < N and board[idx1 + 1][idx2] == board[idx1 + 1][idx2 + 1] == 0:
                    dfs(idx1 + 1, idx2 + 1, 1)

        elif status == 1:
            if idx2 + 1 < N and board[idx1][idx2 + 1] == 0:
                dfs(idx1, idx2 + 1, 0)

                if idx1 + 1 < N and board[idx1 + 1][idx2] == board[idx1 + 1][idx2 + 1] == 0:
                    dfs(idx1 + 1, idx2 + 1, 1)

            if idx1 + 1 < N and board[idx1 + 1][idx2] == 0:
                dfs(idx1 + 1, idx2, 2)

        else:
            if idx1 + 1 < N and board[idx1 + 1][idx2] == 0:
                dfs(idx1 + 1, idx2, 2)

                if idx2 + 1 < N and board[idx1][idx2 + 1] == board[idx1 + 1][idx2 + 1] == 0:
                    dfs(idx1 + 1, idx2 + 1, 1)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
dfs(0, 1, 0)
print(cnt)
