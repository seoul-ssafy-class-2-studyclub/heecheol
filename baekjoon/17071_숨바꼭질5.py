import collections
import sys
sys.stdin = open('input.txt', 'r')


N, K = map(int, input().split())
visit_even = [0] * 500001
visit_odd = [0] * 500001

time = 0
flag = False
queue = collections.deque([N])
# 5, 7
while queue:

    if time % 2:
        for i in range(len(queue)):
            cur = queue.popleft()
            visit_odd[cur] = 1
            nxts = [cur - 1, cur + 1, 2 * cur]
            for nxt in nxts:
                if 0 <= nxt <= 500000 and visit_odd[nxt] is 0:
                    queue.append(nxt)

            if visit_odd[K] == 1:
                flag = True
                break
        if flag is True:
            break

    else:
        for i in range(len(queue)):
            cur = queue.popleft()
            visit_even[cur] = 1
            nxts = [cur - 1, cur + 1, 2 * cur]
            for nxt in nxts:
                if 0 <= nxt <= 500000 and visit_even[nxt] is 0:
                    queue.append(nxt)

            if visit_even[K] == 1:
                flag = True
                break
        if flag is True:
            break

    time += 1
    K += time
    if K > 500000:
        break

if flag is True:
    print(time)
else:
    print(-1)