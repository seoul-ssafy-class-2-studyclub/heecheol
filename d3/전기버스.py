import sys
sys.stdin = open('input.txt', 'r')

for T in range(int(input())):
    K, N, M = map(int, input().split())
    charger = list(map(int, input().split()))

    count = 0
    start = 0
    flag = True

    while flag:
        for k in range(K, 0, -1):   # K부터 K-1, ..., 1까지
            if start + k == N:  # 현재 상태에 그 값을 더했을 때 마지막에 도달하면
                flag = False
                break

            elif start + k in charger:  # 현재에서 그 값을 더한 수가 charger 리스트안에 있으면
                start = start + k
                count += 1
                break
        else:
            count = 0
            break

    print('#{} {}'.format(T+1, count))
    