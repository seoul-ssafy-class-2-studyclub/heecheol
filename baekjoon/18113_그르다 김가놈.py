import heapq
import sys
sys.stdin = open('input.txt', 'r')

N, K, M = map(int, input().split())
heap = []
total = 0
for i in range(N):
    origin = int(input())
    if origin <= K:
        continue
    elif origin < 2 * K:
        heapq.heappush(heap, (-(origin - K), origin - K))
        total += origin - K
    else:
        heapq.heappush(heap, (-(origin - 2 * K), origin - 2 * K))
        total += origin - 2 * K

p_limit = min(total // M, heap[0][1])

flag = False
for p in range(p_limit, 0, -1):
    kimbab = heap[:]
    heapq.heapify(kimbab)
    cnt = 0
    while kimbab:
        n = heapq.heappop(kimbab)[1] // p
        if n == 0:
            break

        else:
            cnt += n

        if cnt >= M:
            flag = True
            break

    if flag is True:
        break

if flag is True:
    print(p)
else:
    print(-1)
