import heapq
import sys
sys.stdin = open('input.txt', 'r')

R, C, M = map(int, input().split())     # row, col, amount
sharks = [list(map(int, input().split())) for _ in range(M)]

d_change = {1: 2, 2: 1, 3: 4, 4: 3}
total = 0
man = 1     # person location

# while

# 낚시
same_col = []
for i in range(len(sharks)):
    r, c, s, d, z = sharks[i]
    if c == man:
        heapq.heappush(same_col, (r, z, i))
if len(same_col) != 0:
    caught = heapq.heappop(same_col)
    sharks.pop(caught[2])
    total += caught[1]      # + kilogram
# 이동, check board
board = [[[] for _ in range(C)] for _ in range(R)]
for i in range(len(sharks)):
    r, c, s, d, z = sharks[i]



# 중복 제거


