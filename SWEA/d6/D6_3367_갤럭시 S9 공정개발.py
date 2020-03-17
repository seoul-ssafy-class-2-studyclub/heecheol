import heapq
import sys
sys.stdin = open('input.txt', 'r')


for T in range(int(input())):
    N = int(input())
    costs = list(map(int, input().split()))

    queue = []
    heapq.heappush(queue, (0, costs))

    result = float('inf')

    while queue:
        cost, arr = heapq.heappop(queue)

        while queue:
            if (cost, arr) == queue[0]:
                heapq.heappop(queue)
            else:
                break

        if len(arr) == 2:
            temp = cost + sum(arr)
            if temp < result:
                result = temp
            continue

        for i in range(len(arr) - 1):
            temp = arr[i] + arr[i + 1]
            if temp + cost >= result:
                continue
            n_arr = arr[:i] + [temp] + arr[i + 2:]
            heapq.heappush(queue, (cost + temp, n_arr))

    print('#{} {}'.format(T + 1, result))
