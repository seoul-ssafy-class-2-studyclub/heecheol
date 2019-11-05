import collections
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    visit = [False] * 1000001
    temp1 = [N]
    flag = True
    cnt = 0
    while flag:
        cnt += 1
        temp2 = []
        for num in temp1:
            n1 = num + 1
            if n1 <= 1000000 and visit[n1] is False:
                if n1 == M:
                    flag = False
                    break
                visit[n1] = True
                temp2.append(n1)

            n2 = num - 1
            if n2 > 0 and visit[n2] is False:
                if n2 == M:
                    flag = False
                    break
                visit[n2] = True
                temp2.append(n2)

            n3 = num * 2
            if n3 <= 1000000 and visit[n3] is False:
                if n3 == M:
                    flag = False
                    break
                visit[n3] = True
                temp2.append(n3)

            n4 = num - 10
            if n4 > 0 and visit[n4] is False:
                if n4 == M:
                    flag = False
                    break
                visit[n4] = True
                temp2.append(n4)

        temp1 = temp2

    # print(dp)
    print('#{} {}'.format(tc, cnt))
