import collections
import sys
sys.stdin = open('input.txt', 'r')


def skill_reverse(j, s):
    global top
    global bottom
    if s == 1:
        for k in range(top, bottom - 1, -1):
            if init_card[k] == 0:
                init_card[k] = j
                top = k - 1
                return
    elif s == 2:
        cnt = 0
        for k in range(top, bottom - 1, -1):
            if init_card[k] == 0:
                cnt += 1
                if cnt == 2:
                    init_card[k] = j
                    return
                else:
                    top = k
    else:
        for k in range(bottom, top + 1):
            if init_card[k] == 0:
                init_card[k] = j
                bottom = k + 1
                return


N = int(input())
skill_info = list(map(int, input().split()))
init_card = collections.deque([0] * N)
top = N - 1
bottom = 0
for i in range(N):
    skill_reverse(N - i, skill_info[i])

init_card.reverse()

print(' '.join(map(str, init_card)))
