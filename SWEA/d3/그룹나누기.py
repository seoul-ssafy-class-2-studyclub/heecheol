import sys

sys.stdin = open('input.txt', 'r')


def make_set(n):
    return [x for x in range(n + 1)]


def find_set(x):
    if x == arr[x]:
        return x
    else:
        return find_set(arr[x])


def union(x, y):
    arr[find_set(y)] = find_set(x)


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = make_set(N)

    inputs = list(map(int, input().split()))
    for _ in range(M):
        a = inputs.pop(0)
        b = inputs.pop(0)
        if a < b:
            union(a, b)
        else:
            union(b, a)

    for i in range(1, N + 1):
        arr[i] = find_set(i)

    print('#{} {}'.format(tc, len(set(arr)) - 1))
