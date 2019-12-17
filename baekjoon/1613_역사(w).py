# wrong

import sys
sys.stdin = open('input.txt', 'r')


def is_connect(a, b):

    while True:
        if parent[b] == a:
            return True
        if parent[b] == b:
            return False
        b = parent[b]


n, k = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(k):
    i, j = map(int, input().split())
    if is_connect(i, j):
        continue
    else:
        parent[j] = i

s = int(input())
result = []

for _ in range(s):
    i, j = map(int, input().split())
    if is_connect(i, j):
        result.append(str(-1))
    elif is_connect(j, i):
        result.append(str(1))
    else:
        result.append(str(0))

print('\n'.join(result))
