import sys
sys.stdin = open('input.txt', 'r')


N, M, V = map(int, input().split())

v_dfs = [False] * (N + 1)
v_bfs = [False] * (N + 1)

board = [[] for _ in range(N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    board[i].append(j)
    board[j].append(i)

result_dfs = []
result_bfs = []

stack = [V]
while stack:
    node = stack.pop()
    if v_dfs[node] is False:
        v_dfs[node] = True
        result_dfs.append(str(node))
        temp = sorted(board[node], reverse=True)
        stack.extend(temp)

queue = [V]
while queue:
    node = queue.pop(0)
    if v_bfs[node] is False:
        v_bfs[node] = True
        result_bfs.append(str(node))
        temp = sorted(board[node])
        queue.extend(temp)

print(' '.join(result_dfs))
print(' '.join(result_bfs))
