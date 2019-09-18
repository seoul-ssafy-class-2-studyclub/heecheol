import sys
import itertools
sys.stdin = open('input_1.txt', 'r')

def ch_chic(idx, ls):
   global M
   if len(ls) == M:
       if ls not in chosen:
           chosen.append(ls)
       return 0
   for j in range(idx+1, len(stores)):
       ch_chic(j, ls+[stores[j]])

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]

houses = []
stores = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '1':
            houses.append((i, j))
        elif board[i][j] == '2':
            stores.append((i, j))
chosen = []
for i in range(len(stores)):
   ch_chic(i,[stores[i]])
#
# chosen = list(itertools.combinations(stores, M))
min_distance = 999999
for store3 in chosen:
    total = 0
    for house in houses:
        distance = 99999
        for store in store3:
            temp = abs(store[0] - house[0]) + abs(store[1] - house[1])
            if temp < distance:
                distance = temp
        total += distance
    if total < min_distance:
        min_distance = total
print(min_distance)

