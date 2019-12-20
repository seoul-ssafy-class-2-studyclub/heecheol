import sys
sys.stdin = open('input.txt', 'r')


t = int(input())
result = []
for tc in range(t):
    n = int(input())

    locations = [(0, 0)] * (n + 2)

    hi, hj = map(int, input().split())
    locations[0] = (hi, hj)

    for i in range(1, n + 1):
        si, sj = map(int, input().split())
        locations[i] = (si, sj)

    fi, fj = map(int, input().split())
    locations[n + 1] = (fi, fj)

    connect = [[0] * (n + 2) for _ in range(n + 2)]
    for i in range(n + 1):
        for j in range(i + 1, n + 2):
            D = abs(locations[i][0] - locations[j][0]) + abs(locations[i][1] - locations[j][1])
            if D <= 1000:
                connect[i][j] = connect[j][i] = 1

    for k in range(1, n + 1):
        for i in range(n + 1):
            if connect[i][k] == 0:
                continue

            for j in range(i + 1, n + 2):
                if i == j or connect[i][j] == 1 or connect[k][j] == 0:
                    continue
                connect[i][j] = connect[j][i] = 1

    if connect[0][n + 1] == 1:
        result.append('happy')
    else:
        result.append('sad')

print('\n'.join(result))
