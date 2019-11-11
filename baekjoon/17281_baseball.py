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
            result[j][order[i]] = results[j][i]
    s = 0
    points = 0
    for inning in range(N):
        this_inning = result[inning][s:] + result[inning][:s]
        play = ''.join(this_inning)
        s = 0

        if dp.get(play) is None:
            outs = 0
            p_str = ''
            while outs < 3:
                if this_inning[s] == '0':
                    outs += 1
                elif this_inning[s] == '1':
                    p_str += '1'
                elif this_inning[s] == '2':
                    p_str += '10'
                elif this_inning[s] == '3':
                    p_str += '100'
                else:
                    p_str += '1000'
                if s == 8:
                    s = 0
                else:
                    s += 1
            point = p_str[:-3].count('1')
            dp[play] = (point, s)
        else:
            point, s = dp[play]
        points += point

    if points > max_point:
        max_point = points
print(max_point)
# print(dp)
