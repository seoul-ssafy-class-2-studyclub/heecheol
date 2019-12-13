import sys
sys.stdin = open('input.txt', 'r')


def init(node, start, end):

    if start == end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]


def update(node, start, end, idx, diff):
    if idx < start or idx > end:
        return
    tree[node] += diff
    if start != end:
        update(node * 2, start, (start + end) // 2, idx, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, idx, diff)


def subsum(node, start, end, left, right):

    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return subsum(node * 2, start, (start + end) // 2, left, right) + subsum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    tree = [0] * 4 * N
    l = list(map(int, input().split()))

    init(1, 0, N - 1)
    result = []
    # print(tree)

    for _ in range(M):
        C, A, B = map(int, input().split())

        if C == 1:
            l[A - 1] += B
            update(1, 0, N - 1, A - 1, B)
            # print(tree)
        else:   # C == 2
            temp = subsum(1, 0, N - 1, A - 1, B - 1)
            result.append(str(temp))

    print('#{} {}'.format(tc, ' '.join(result)))
