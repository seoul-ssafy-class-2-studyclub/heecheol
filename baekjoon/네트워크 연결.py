import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
print(adj_list)


