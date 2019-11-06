import heapq
import sys
sys.stdin = open('input.txt', 'r')


def jump(cur, dist, fee):

    global min_fee

    if fee >= min_fee:
        return

    elif cur == N - 1:
        min_fee = fee

    else:
        if cur + dist <= N - 2:
            jump(cur + dist + 1, dist + 1, fee + board[cur + dist + 1])

        if cur >= dist:
            jump(cur - dist, dist, fee + board[cur - dist])

import heapq
N = int(input())
board = [0] * N

for i in range(N):
    board[i] = int(input())
# min_fee = 9876543210

# jump(1, 1, board[1])
arr = []
heapq.heappush(arr, (board[1], 1, 1))


while True:
    fee, cur, dist = heapq.heappop(arr)
    if cur == N - 1:
        break

    if cur + dist <= N - 2:
        heapq.heappush(arr, (fee + board[cur + dist + 1], cur + dist + 1, dist + 1))

    if cur >= dist:
        heapq.heappush(arr, (fee + board[cur - dist], cur - dist, dist))

print(fee)
