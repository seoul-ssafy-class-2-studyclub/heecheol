import itertools
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
board = [input().split() for _ in range(N)]
zero = []

for i in range(N):
    for j in range(M):
        if board[i][j] == '0':
            zero.append((i, j))
        
zero_combination = list(itertools.combinations(zero, 3))

adj_list = [(0, -1), (1, 0), (0, 1), (-1, 0)]
max_cnt = 0
for walls in zero_combination:
    board2 = [row[:] for row in board]
    for w in range(3):
        idx1, idx2 = walls[w]
        board2[idx1][idx2] = '1'
    
    for i in range(N):
        for j in range(M):
            if board2[i][j] == '2':
                stack = [[i, j]]
                while stack:
                    row, col = stack.pop()
                    if board2[row][col] != '1':
                        board2[row][col] = '1'
                        for adj in adj_list:
                            nxt_r = row + adj[0]
                            nxt_c = col + adj[1]
                            if 0 <= nxt_r < N and 0 <= nxt_c < M:
                                if board2[nxt_r][nxt_c] != '1':
                                    stack.append([nxt_r, nxt_c])
    cnt = 0                            
    for i in range(N):
        for j in range(M):
            if board2[i][j] == '0':
                cnt += 1
    if cnt > max_cnt:
        max_cnt = cnt    
print(max_cnt)
