import sys
sys.stdin = open('input.txt', 'r')


hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    data = list(input())

    length = N // 4
    data += data[:length]
    passwords = []
    results = []

    for s in range(length):
        for n in range(4):
            edge = data[length * n + s:length * (n + 1) + s]
            value = 0
            for i in range(length):
                value += hex[edge[i]] * (16 ** (length - i - 1))

            if value not in results:
                results.append(value)

    print('#{} {}'.format(tc, sorted(results, reverse=True)[K - 1]))