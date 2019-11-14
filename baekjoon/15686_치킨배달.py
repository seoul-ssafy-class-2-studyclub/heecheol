import itertools
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

houses = []
stores = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            houses.append((i, j))
        elif board[i][j] == 2:
            stores.append((i, j))

# step1 => combination (M)
# step2 => for houses => min ( sum ( min ( distance )))
result = 987654321

comb_stores = list(itertools.combinations(stores, M))
for comb_store in comb_stores:
    total = 0
    for house in houses:
        h_row, h_col = house
        arr_distance = []
        for store in comb_store:
            arr_distance.append(abs(h_row - store[0]) + abs(h_col - store[1]))
        total += min(arr_distance)
        if total > result:
            break
    if total < result:
        result = total
print(result)
