import collections
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
dp = [0] * (N + 1)
queue = collections.deque([(N, [])])

while queue:
    num, vis = queue.popleft()
    if num == 0:
        break
    if 0 < num < N + 1 and dp[num] == 0:
        dp[num] = 1
        if num + 2 < N and dp[num + 2] == 0:
            queue.append((N + 2, ['[-]'] + vis))

        if num - 2 >= 0 and dp[num - 2] == 0:
            queue.append((N - 2, vis + ['[+]']))

        if num % 2 == 0 and dp[num // 2] == 0:
            queue.append((N // 2, vis + ['[*]']))

        if num * 2 < N and dp[num * 2] == 0:
            queue.append((N * 2, vis + ['[/]']))

print(vis)