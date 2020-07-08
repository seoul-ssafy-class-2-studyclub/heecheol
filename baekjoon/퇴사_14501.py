import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
works = [0] * N

for i in range(N):
    works[i] = list(map(int, input().split()))

queue = [(0, 0)]
result = 0
while queue:
    day, money = queue.pop(0)

    if money > result:
        result = money

    for k in range(day, N):
        next_day = k + works[k][0]
        if next_day <= N:
            queue.append((next_day, money + works[k][1]))

print(result)
