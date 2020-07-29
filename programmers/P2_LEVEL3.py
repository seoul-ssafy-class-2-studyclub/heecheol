def solution(board):
    N = len(board)
    visit = [[[False, False] for _ in range(N)] for __ in range(N)]
    visit[0][0][0] = True

    def move(i, j, k):
        if k == 0:
            if j > 0 and board[i][j-1] == 0 and visit[i][j-1][0] is False:
                visit[i][j-1][0] = True
                queue.append((i, j-1, 0))
            if j < N-2 and board[i][j+2] == 0 and visit[i][j+1][0] is False:
                visit[i][j+1][0] = True
                queue.append((i, j+1, 0))
            if i > 0 and board[i-1][j] == 0 and board[i-1][j+1] == 0:
                if visit[i-1][j][0] is False:
                    visit[i-1][j][0] = True
                    queue.append((i-1, j, 0))
                if visit[i-1][j][1] is False:
                    visit[i-1][j][1] = True
                    queue.append((i-1, j, 1))
                if visit[i-1][j+1][1] is False:
                    visit[i-1][j+1][1] = True
                    queue.append((i-1, j+1, 1))
            if i < N-1 and board[i+1][j] == 0 and board[i+1][j+1] == 0:
                if visit[i][j][1] is False:
                    visit[i][j][1] = True
                    queue.append((i, j, 1))
                if visit[i][j+1][1] is False:
                    visit[i][j+1][1] = True
                    queue.append((i, j+1, 1))
                if visit[i+1][j][0] is False:
                    visit[i+1][j][0] = True
                    queue.append((i+1, j, 0))
        else:
            if j > 0 and board[i][j-1] == 0 and board[i+1][j-1] == 0:
                if visit[i][j-1][0] is False:
                    visit[i][j-1][0] = True
                    queue.append((i, j-1, 0))
                if visit[i][j-1][1] is False:
                    visit[i][j-1][1] = True
                    queue.append((i, j-1, 1))
                if visit[i+1][j-1][0] is False:
                    visit[i+1][j-1][0] = True
                    queue.append((i+1, j-1, 0))
            if j < N-1 and board[i][j+1] == 0 and board[i+1][j+1] == 0:
                if visit[i][j+1][1] is False:
                    visit[i][j+1][1] = True
                    queue.append((i, j+1, 1))
                if visit[i][j][0] is False:
                    visit[i][j][0] = True
                    queue.append((i, j, 0))
                if visit[i+1][j][0] is False:
                    visit[i+1][j][0] = True
                    queue.append((i+1, j, 0))
            if i > 0 and board[i-1][j] == 0 and visit[i-1][j][1] is False:
                visit[i-1][j][1] = True
                queue.append((i-1, j, 1))
            if i < N-2 and board[i+2][j] == 0 and visit[i+1][j][1] is False:
                visit[i+1][j][1] = True
                queue.append((i+1, j, 1))
        return

    queue = [(0, 0, 0)]
    answer = 0
    while queue:
        answer += 1
        for _ in range(len(queue)):
            a, b, c = queue.pop(0)
            move(a, b, c)
        if visit[N-1][N-2][0] or visit[N-2][N-1][1]:
            return answer


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
