import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    print(A)
    print(B)

    mA = (N - 1) // 2
    mB = (N - 1) // 2