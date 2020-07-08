import sys
sys.stdin = open('input.txt', 'r')
import itertools


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = float('inf')

people_all = list(range(N))
for team_start in itertools.combinations(people_all, N // 2):
    team_link = list(set(people_all) - set(team_start))

    stat_start = 0
    stat_link = 0
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            stat_start += board[team_start[i]][team_start[j]] + board[team_start[j]][team_start[i]]
            stat_link += board[team_link[i]][team_link[j]] + board[team_link[j]][team_link[i]]

    diff = abs(stat_start - stat_link)
    if diff < result:
        result = diff
        if diff == 0:
            break

print(result)
