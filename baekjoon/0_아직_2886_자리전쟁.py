from pprint import pprint
import heapq
import sys
sys.stdin = open('input.txt', 'r')


R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

seats = []
people = []

for i in range(R):
    for j in range(C):
        if board[i][j] == '.':
            continue
        elif board[i][j] == 'L':
            seats.append((i, j))
        else:
            people.append((i, j))

queue = []
inf = float('inf')

for s1, s2 in seats:
    for p1, p2 in people:
        heapq.heappush(queue, (((s1 - p1) ** 2 + (s2 - p2) ** 2), (s1, s2), (p1, p2)))

# print(queue)

visit_s = [[inf] * C for _ in range(R)]
visit_f = [[0] * C for _ in range(R)]
visit_p = [[0] * C for _ in range(R)]

cnt = 0

while queue:
    D, seat, person = heapq.heappop(queue)
    if visit_p[person[0]][person[1]] == 0:
        if D <= visit_s[seat[0]][seat[1]]:
            visit_s[seat[0]][seat[1]] = D
            visit_p[person[0]][person[1]] = 1
            visit_f[seat[0]][seat[1]] += 1
            if visit_f[seat[0]][seat[1]] == 2:
                cnt += 1

print(cnt)
# print('\n fight')
# pprint(visit_f)
# print('\n people')
# pprint(visit_p)
# print('\n seat')
# pprint(visit_s)
