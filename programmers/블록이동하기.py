from pprint import pprint
import collections

def solution(board):
    answer = 0
    n = len(board)

    visit = [[[0] * 4 for _ in range(n)] for _ in range(n)]  # up, right, down, left

    init = (0, 0, 0, 1)
    visit[0][0][1] = visit[0][1][3] = 1

    queue = collections.deque([init])
    flag = False
    while queue:
        print(answer)
        for _ in range(len(queue)):
            x1, y1, x2, y2 = queue.popleft()
            print(x1, y1, x2, y2)

            if x2 == y2 == n - 1:
                flag = True
                break

            if x1 == x2:    # y1 < y2
                if visit[x2][y2][1] == 0:
                    if y2 + 1 < n and board[x2][y2 + 1] == 0:
                        visit[x2][y2][1] = visit[x2][y2 + 1][3] = 1
                        queue.append((x2, y2, x2, y2 + 1))
                if visit[x1][y1][3] == 0:
                    if y1 > 0 and board[x1][y1 - 1] == 0:
                        visit[x1][y1 - 1][1] = visit[x1][y1][3] = 1
                        queue.append((x1, y1 - 1, x1, y1))
                if x1 > 0 and board[x1 - 1][y1] == 0 and board[x2 - 1][y2] == 0:
                    if visit[x1][y1][0] == 0:
                        visit[x1][y1][0] = visit[x1 - 1][y1][2] = 1
                        queue.append((x1 - 1, y1, x1, y1))
                    if visit[x1 - 1][y1][1] == 0:
                        visit[x1 - 1][y1][1] = visit[x2 - 1][y2][3] = 1
                        queue.append((x1 - 1, y1, x2 - 1, y2))
                    if visit[x2][y2][0] == 0:
                        visit[x2 - 1][y2][2] = visit[x2][y2][0] = 1
                        queue.append((x2 - 1, y2, x2, y2))
                if x1 + 1 < n and board[x1 + 1][y1] == 0 and board[x2 + 1][y2] == 0:
                    if visit[x1][y1][2] == 0:
                        visit[x1][y1][2] = visit[x1 + 1][y1][0] = 1
                        queue.append((x1, y1, x1 + 1, y1))
                    if visit[x1 + 1][y1][1] == 0:
                        visit[x1 + 1][y1][1] = visit[x2 + 1][y2][3] = 1
                        queue.append((x1 + 1, y1, x2 + 1, y2))
                    if visit[x2][y2][2] == 0:
                        visit[x2][y2][2] = visit[x2 + 1][y2][0] = 1
                        queue.append((x2, y2, x2 + 1, y2))

            else:
                if visit[x1][y1][0] == 0:
                    if x1 > 0 and board[x1 - 1][y1] == 0:
                        visit[x1][y1][0] = visit[x1 - 1][y1][2] = 1
                        queue.append((x1 - 1, y1, x1, y1))
                if visit[x2][y2][2] == 0:
                    if x2 + 1 < n and board[x2 + 1][y2] == 0:
                        visit[x2 + 1][y2][0] = visit[x2][y2][2] = 1
                        queue.append((x2, y2, x2 + 1, y2))
                if y1 > 0 and board[x1][y1 - 1] == 0 and board[x2][y1 - 1] == 0:
                    if visit[x1][y1][3] == 0:
                        visit[x1][y1][3] = visit[x1][y1 - 1][1] = 1
                        queue.append((x1, y1 - 1, x1, y1))
                    if visit[x1][y1 - 1][2] == 0:
                        visit[x1][y1 - 1][2] = visit[x2][y2 - 1][0] = 1
                        queue.append((x1, y1 - 1, x2, y2 - 1))
                    if visit[x2][y2][3] == 0:
                        visit[x2][y2][3] = visit[x2][y2 - 1][1] = 1
                        queue.append((x2, y2 - 1, x2, y2))

                if y1 + 1 < n and board[x1][y1 + 1] == 0 and board[x2][y2 + 1] == 0:
                    if visit[x1][y1][1] == 0:
                        visit[x1][y1][1] = visit[x1][y1 + 1][3] = 1
                        queue.append((x1, y1, x1, y1 + 1))
                    if visit[x1][y1 + 1][2] == 0:
                        visit[x1][y1 + 1][2] = visit[x2][y2 + 1][0] = 1
                        queue.append((x1, y1 + 1, x2, y2 + 1))
                    if visit[x2][y2][1] == 0:
                        visit[x2][y2][1] = visit[x2][y2 + 1][3] = 1
                        queue.append((x2, y2, x2, y2 + 1))

        if flag:
            break

        answer += 1

    # print(answer)
    return answer


input_board = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
solution(input_board)
