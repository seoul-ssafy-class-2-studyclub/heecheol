import itertools
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
results = [input().split() for _ in range(N)]
orders = list(itertools.permutations(list(range(1, 9)), 8))
dp = {}
max_point = 0

for order in orders:
    order = list(order)
    order.insert(3, 0)
    result = [[0] * 9 for _ in range(N)]

    for i in range(9):
        for j in range(N):
            result[j][i] = results[j][order[i]]

    s = 0
    points = 0
    for inning in range(N):
        this_inning = result[inning]
        play = ''.join(result[inning][s:] + result[inning][:s])

        if dp.get(play) is None:
            e = s
            outs = 0
            point = 0
            three, two, one = 0, 0, 0
            while outs < 3:
                if this_inning[e] == '0':
                    outs += 1
                elif this_inning[e] == '1':
                    point += three
                    three, two, one = two, one, 1
                elif this_inning[e] == '2':
                    point += two + three
                    three, two, one = one, 1, 0
                elif this_inning[e] == '3':
                    point += one + two + three
                    three, two, one = 1, 0, 0
                else:
                    point += one + two + three + 1
                    three, two, one = 0, 0, 0
                if e == 8:
                    e = 0
                else:
                    e += 1
            dp[play] = (point, (e - s + 9) % 9)
            s = e
        else:
            point, e = dp[play]
            s = (s + e) % 9
        points += point

    if points > max_point:
        max_point = points

print(max_point)
print(dp)