import heapq
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
result = ['?'] * T
for tc in range(T):
    n = int(input())
    order = list(map(int, input().split()))

    board = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n - 1):
        for j in range(i + 1, n):
            board[order[j]][order[i]] = 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())
        board[a][b], board[b][a] = board[b][a], board[a][b]

    temp = [0] * n
    sums = []

    for r in range(1, len(board)):
        heapq.heappush(sums, (sum(board[r]), r))

    for i in range(n):
        a, b = heapq.heappop(sums)
        if a == i:
            temp[i] = str(b)
            continue
        elif a > i:
            result[tc] = 'IMPOSSIBLE'
            break
        else:
            break
    else:
        result[tc] = ' '.join(temp)

print('\n'.join(result))
