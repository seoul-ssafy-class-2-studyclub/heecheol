import heapq
import sys
sys.stdin = open('input.txt', 'r')


N, M = map(int, input().split())
nodes = [[] for _ in range(N + 1)]
weights = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    nodes[A].append(B)
    nodes[B].append(A)
    weights[A][B] = weights[B][A] = C

start_node, end_node = map(int, input().split())

visit = [False] * (N + 1)
# nodes[start_node]

queue = []

