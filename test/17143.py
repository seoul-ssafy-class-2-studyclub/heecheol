import sys
sys.stdin = open('17143.txt', 'r')


def catch(p_col):
    stack1 = []
    i_shark = 0
    for m in range(1, M+1):
        if alive[m] == 1 and cl[m] == p_col:
            stack1.append(m)
    if len(stack1) != 0:
        distance = 500
        for i in stack1:
            if rl[i] < distance:
                distance = rl[i]
                i_shark = i
        alive[i_shark] = 0


def move():
    for m in range(1, M+1):
        if alive[m] == 1:
            if dl[m] == 1 or dl[m] == 2:
                moving = sl[m] % (R*2-2)
                for i in range(moving):
                    if dl[m] == 1 and rl[m] == 1:
                        dl[m] = 2
                        rl[m] += 1
                    elif dl[m] == 2 and rl[m] == R:
                        dl[m] = 1
                        rl[m] -= 1
                    elif dl[m] == 1:
                        rl[m] -= 1
                    else:
                        rl[m] += 1

            else:
                moving = sl[m] % (C*2-2)
                for i in range(moving):
                    if dl[m] == 3 and cl[m] == C:
                        dl[m] = 4
                        cl[m] -= 1
                    elif dl[m] == 4 and cl[m] == 1:
                        dl[m] = 3
                        cl[m] += 1
                    elif dl[m] == 3:
                        cl[m] += 1
                    else:
                        cl[m] -= 1


def fight():
    for m in range(M):
        if alive[m] == 1:
            for other in range(M):
                if alive[other] == 1 and other != m and rl[m] == rl[other] and cl[m] == cl[other]:
                    if zl[m] > zl[other]:
                        alive[other] = -1
                    else:
                        alive[m] = -1
                        break


R, C, M = map(int, input().split())

rl = [0]*(M+1)
cl = [0]*(M+1)
sl = [0]*(M+1)      # speed
dl = [0]*(M+1)      # 1 up / 2 down / 3 right / 4 left
zl = [0]*(M+1)      # size

alive = [1]*(M+1)   # 1 alive / 0 caught / -1 eaten

for m in range(1, M+1):
    rl[m], cl[m], sl[m], dl[m], zl[m] = map(int, input().split())

person_col = 1

while True:
    catch(person_col)
    move()
    fight()

    if person_col == C:
        break
    person_col += 1

sum_size = 0
for m in range(1, M+1):
    if alive[m] == 0:
        sum_size += zl[m]
print(sum_size)
