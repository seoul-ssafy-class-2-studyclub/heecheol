import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
visit = [True] * 2 + [False] * (M - 1)
result = []
for n in range(2, M + 1):
    if visit[n] is False:
        if n >= N:
            result.append(str(n))
        i = 2
        while n * i <= M:
            visit[n * i] = True
            i += 1

print('\n'.join(result))
