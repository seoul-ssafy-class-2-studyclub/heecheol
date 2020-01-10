import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
M = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
cities = list(set(list(map(int, input().split()))))
visit = [False] * N

start = cities[0] - 1
queue = [start]
visit[start] = True

while queue:
    city = queue.pop(0)
    for n in range(N):
        if visit[n] is False and board[city][n] == 1:
            visit[n] = True
            queue.append(n)
flag = True
for c in cities:
    if visit[c - 1] is False:
        flag = False
        break

if flag is True:
    print('YES')
else:
    print('NO')
