import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))

    nearest = abs(numbers[0])
    cnt = 1
    for i in range(1, len(numbers)):
        if nearest > abs(numbers[i]):
            nearest = abs(numbers[i])
            cnt = 1
        elif nearest == abs(numbers[i]):
            cnt += 1
    print(f'#{tc+1} {nearest} {cnt}')
    