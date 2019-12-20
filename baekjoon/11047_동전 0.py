import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
coin = [0] * N
for i in range(N):
    coin[N - i - 1] = int(input())

result = 987654321
for i in range(N):
    idx = i
    change = K
    cnt = 0
    while cnt < result:
        if change == 0:
            result = cnt
            break
        cnt += change // coin[idx]
        change %= coin[idx]
        idx += 1

print(result)
