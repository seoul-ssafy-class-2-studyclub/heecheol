def solution(board, moves):
    N = len(board)
    new_board = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[j][i] != 0:
                new_board[i].append(board[j][i])
        new_board[i].reverse()


    stack = []
    cnt = 0

    for m in moves:
        if len(new_board[m - 1]) != 0:
            doll = new_board[m - 1].pop()
            stack.append(doll)
            if len(stack) > 1 and stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                cnt += 2

    answer = cnt
    return answer

board_input = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves_input = [1,5,3,5,1,2,1,4]

print(solution(board_input, moves_input))