import math
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
people = list(map(int, input().split()))

B, C = map(int, input().split())
cnt = 0
for i in range(N):
    people[i] -= B
    if people[i] <= 0:
        cnt += 1
    else:
        cnt += math.ceil(people[i] / C) + 1

print(cnt)
