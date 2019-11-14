import itertools
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

people = list(range(N))

team_A_list = list(itertools.combinations(people, N // 2))
everyone = set(people)

difference = []

for team_A in team_A_list:
    team_B = list(everyone - set(team_A))

    point_A = 0
    point_B = 0

    nn = N // 2

    for i in range(nn - 1):
        for j in range(i + 1, nn):
            point_A += board[team_A[i]][team_A[j]] + board[team_A[j]][team_A[i]]

    for i in range(nn - 1):
        for j in range(i + 1, nn):
            point_B += board[team_B[i]][team_B[j]] + board[team_B[j]][team_B[i]]

    difference.append(abs(point_A - point_B))

print(min(difference))
