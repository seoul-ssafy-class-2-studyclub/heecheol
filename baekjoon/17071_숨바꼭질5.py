import collections
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
visit_even = [0] * 500001
visit_odd = [0] * 500001
visit_even[N] = 1

time = 0
flag = False
queue = collections.deque([N])

while queue:

    if time % 2:
        if visit_odd[K] == 1:
            flag = True
            break

        for i in range(len(queue)):
            cur = queue.popleft()
            nxts = [cur - 1, cur + 1, 2 * cur]
            for nxt in nxts:
                if 0 <= nxt <= 500000 and visit_even[nxt] is 0:
                    visit_even[nxt] = 1
                    queue.append(nxt)

    else:
        if visit_even[K] == 1:
            flag = True
            break

        for i in range(len(queue)):
            cur = queue.popleft()
            nxts = [cur - 1, cur + 1, 2 * cur]
            for nxt in nxts:
                if 0 <= nxt <= 500000 and visit_odd[nxt] is 0:
                    visit_odd[nxt] = 1
                    queue.append(nxt)

    time += 1
    K += time
    if K > 500000:
        break

if flag is True:
    print(time)
else:
    print(-1)
