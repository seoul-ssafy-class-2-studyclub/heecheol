import sys
sys.stdin = open('input.txt', 'r')


def turn_right(n):
    gears[n].insert(0, gears[n].pop())


def turn_left(n):
    gears[n].append(gears[n].pop(0))


gears = [list(input()) for _ in range(4)]
# print(gears)
for _ in range(int(input())):
    N, D = map(int, input().split())
    N -= 1
    arr = [(N, D)]

    d = D * (-1)
    # 오른쪽 확인하기
    for i in range(N, 3):
        if gears[i][2] != gears[i + 1][6]:
            arr.append((i + 1, d))
            if d == 1:
                d = -1
            else:
                d = 1
        else:
            break

    d = D * (-1)
    # 왼쪽 확인하기
    for j in range(N, 0, -1):
        if gears[j][6] != gears[j - 1][2]:
            arr.append((j - 1, d))
            if d == 1:
                d = -1
            else:
                d = 1
        else:
            break

    for gear in arr:
        if gear[1] == 1:
            turn_right(gear[0])
        else:
            turn_left(gear[0])

result = 0
for i in range(4):
    result += int(gears[i][0]) * (2 ** i)

print(result)
