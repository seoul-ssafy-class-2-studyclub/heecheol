def solution(m, n, board):
    for r in range(m):
        board[r] = list(board[r])

    def find_block():
        blocks = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == ' ':
                    continue
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                    blocks.append((i, j))
        return blocks

    def erasing(blocks):
        cnt = 0

        for i, j in blocks:
            if board[i][j] != ' ':
                board[i][j] = ' '
                cnt += 1
            if board[i+1][j] != ' ':
                board[i+1][j] = ' '
                cnt += 1
            if board[i][j+1] != ' ':
                board[i][j+1] = ' '
                cnt += 1
            if board[i+1][j+1] != ' ':
                board[i+1][j+1] = ' '
                cnt += 1

        for k in range(n):
            for a in range(m-1, 0, -1):
                if board[a][k] == ' ':
                    for b in range(a-1, -1, -1):
                        if board[b][k] != ' ':
                            board[a][k], board[b][k] = board[b][k], board[a][k]
                            break
                    else:
                        break
        return cnt

    answer = 0
    while True:
        # for row in board:
        #     print(row)
        # print()
        matched = find_block()
        if matched:
            answer += erasing(matched)
        else:
            break

    return answer


print(solution(6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']))
