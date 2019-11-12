import itertools
import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
results = [input().split() for _ in range(N)]
orders = list(itertools.permutations(list(range(1, 9)), 8))

for order in orders:
    order = list(order)
    order.insert(3, 0)

    s = 0
    points = 0
    point_list = []
    for inning in range(N):
        this_inning = results[inning]
        outs = 0
        point = 0
        three, two, one = 0, 0, 0
        while outs < 3:
            if this_inning[order[s]] == '0':
                outs += 1

            elif this_inning[order[s]] == '1':
                point += three
                three, two, one = two, one, 1

            elif this_inning[order[s]] == '2':
                point += two + three
                three, two, one = one, 1, 0

            elif this_inning[order[s]] == '3':
                point += one + two + three
                three, two, one = 1, 0, 0

            else:
                point += one + two + three + 1
                three, two, one = 0, 0, 0

            if s == 8:
                s = 0
            else:
                s += 1

        points += point

    point_list.append(points)

print(max(point_list))
