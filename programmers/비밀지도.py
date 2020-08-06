def solution(n, arr1, arr2):
    square = [2**m for m in range(n-1, -1, -1)]
    board = [[' '] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr1[i] // square[j] or arr2[i] // square[j]:
                board[i][j] = '#'
                arr1[i] %= square[j]
                arr2[i] %= square[j]

    for r in range(n):
        board[r] = ''.join(board[r])

    return board


solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
