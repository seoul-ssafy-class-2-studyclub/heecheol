import collections
import sys
sys.stdin = open('input.txt', 'r')


N, A, B = map(int, input().split())

if A % 2 == B % 2:
    queue_A = collections.deque([A])
    queue_B = collections.deque([B])
    flag = True
    y = 1
    while True:
        dx = 2 ** (y - 1)
        visit = [0] * (N + 1)
        if len(queue_A) == 0 or len(queue_B) == 0:
            break

        for _ in range(len(queue_A)):
            a = queue_A.popleft()
            if a - dx > 0 and visit[a - dx] == 0:
                queue_A.append(a - dx)
                visit[a - dx] = 1
            if a + dx <= N and visit[a + dx] == 0:
                queue_A.append(a + dx)
                visit[a + dx] = 1

        for _ in range(len(queue_B)):
            b = queue_B.popleft()
            if b - dx > 0:
                if visit[b - dx] == 1:
                    flag = False
                    break
                elif visit[b - dx] == 0:
                    queue_B.append(b - dx)
                    visit[b - dx] = 2
            if b + dx <= N:
                if visit[b + dx] == 1:
                    flag = False
                    break
                elif visit[b + dx] == 0:
                    queue_B.append(b + dx)
                    visit[b + dx] = 2

        if flag is False:
            break
        else:
            y += 1

    if flag is True:
        print(-1)
    else:
        print(y)
else:
    print(-1)
