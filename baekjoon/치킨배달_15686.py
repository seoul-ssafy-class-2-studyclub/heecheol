import sys
sys.stdin = open('input.txt', 'r')

import itertools


N, M = map(int, input().split())
board = [input().split() for _ in range(N)]

houses = []
stores = []

for i in range(N):
    for j in range(N):
        if board[i][j] == '0':
            continue
        elif board[i][j] == '1':
            houses.append((i, j))
        else:
            stores.append((i, j))

result = float('inf')
chosen = list(itertools.combinations(stores, M))
for opened in chosen:

    total_distance = 0
    for house in houses:
        shortest = float('inf')
        for store in opened:
            distance = abs(house[0] - store[0]) + abs(house[1] - store[1])
            if distance < shortest:
                shortest = distance
        total_distance += shortest

    if total_distance < result:
        result = total_distance

print(result)
