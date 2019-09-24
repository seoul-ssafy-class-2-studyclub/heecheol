import sys
sys.stdin = open('input.txt', 'r')


def quick_sort(ls, re):
    if ls == re:
        pass

    elif ls >= 0 and re >= 1:
        p = ls
        i = ls + 1
        j = re
        while True:
            while i <= re:
                if A[i] > A[p]:
                    break
                i += 1
            while j > ls:
                if A[j] < A[p]:
                    break
                j -= 1
            if i <= j:
                A[i], A[j] = A[j], A[i]
            else:
                A[p], A[j] = A[j], A[p]
                break

        if ls < j:
            quick_sort(ls, j-1)
        if j+1 <= re:
            quick_sort(j+1, re)


for tc in range(1, int(input()) + 1):
    N = int(input())
    A = list(map(int, input().split()))

    quick_sort(0, N-1)
    print('#{} {}'.format(tc, A[N//2]))