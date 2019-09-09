N = int(input())

board = []
row = []
for i in range(N):
    for j in range(N):
        row.append(0)

    board.append(row)
print(board)