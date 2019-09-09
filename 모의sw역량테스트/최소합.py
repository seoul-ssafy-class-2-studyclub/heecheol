import sys
sys.stdin = open('input.txt', 'r')


def path(i=0, j=0):
    global min_value
    if i == N-1 and j == N-1:
        temp = sum(route)
        if temp < min_value:
            min_value = temp 

    else:
        for ne in nxt:
            idx1 = i+ne[0]
            idx2 = j+ne[1]
            if 0 <= idx1 < N and 0 <= idx2 < N:
                
                route.append(board[idx1][idx2])
                path(idx1, idx2)
                route.pop()


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for n in range(N)]
    
    nxt = [[0, 1], [1, 0]]
    route = [board[0][0]]
    ways = []
    min_value = 9999999
    path()
    print(f'#{tc} {min_value}')

