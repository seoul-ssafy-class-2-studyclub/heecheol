import sys
sys.stdin = open('input.txt', 'r')

N, K, M = map(int, input().split())
arr = [0] * N
total = 0
for i in range(N):
    origin = int(input())
    if origin <= K:
        continue
    elif origin < 2 * K:
        arr[i] = origin - K
    else:
        arr[i] = origin - 2 * K

arr.sort(reverse=True)
p = 1
while True:
    cnt = 0
    flag = False
    for i in range(N):
        n = arr[i] // p
        if n == 0:
            break
        cnt += n
        if cnt >= M:
            flag = True
            break
    if flag is False:
        break
    else:
        p += 1

if flag is False and p == 1:
    print(-1)
else:
    print(p - 1)
