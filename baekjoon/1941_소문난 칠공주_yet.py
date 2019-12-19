import collections
import itertools
import sys
sys.stdin = open('input.txt', 'r')

board = [list(input()) for _ in range(5)]
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
s_group = []
y_group = []
for i in range(5):
    for j in range(5):
        if board[i][j] == 'S':
            s_group.append((i, j))
        else:
            y_group.append((i, j))

cnt = 0
for people_s in range(4, len(s_group) + 1):
    for s_chosen in itertools.combinations(s_group, people_s):
        # print(s_chosen)
        for y_chosen in itertools.combinations(y_group, 7 - people_s):
            people = list(s_chosen) + list(y_chosen)
            board2 = [[0] * 5 for _ in range(5)]
            for person in people:
                board2[person[0]][person[1]] = 1

            queue = collections.deque([people.pop()])
            while queue:
                idx1, idx2 = queue.pop()



print(cnt)