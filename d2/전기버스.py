import sys
sys.stdin = open('input.txt', 'r')

for T in range(int(input())):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    count = 0
    start = 0
    flag = True

    while flag:
        for k in range(K, 0, -1):
            if start + k == N:
                flag = False
                break

            elif start + k in charger:
                start = start + k
                count += 1
                break
        else:
            count = 0
            break

    print('#{} {}'.format(T+1, count))