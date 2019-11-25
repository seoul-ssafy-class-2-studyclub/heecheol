import collections
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
data1 = list(map(int, input().split()))
queue = collections.deque(data1[1:])

parties = [list(map(int, input().split())) for _ in range(M)]
visit = [False] * (N + 1)

while queue:
    person = queue.popleft()
    if visit[person] is False:
        visit[person] = True
        for i in range(len(parties) - 1, -1, -1):
            if person in parties[i][1:]:
                for j in range(1, parties[i][0] + 1):
                    if visit[parties[i][j]] is False:
                        queue.append(parties[i][j])
                parties.pop(i)
                M -= 1
print(M)
