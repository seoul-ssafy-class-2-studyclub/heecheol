import sys
sys.stdin = open('input.txt', 'r')

def move(ix, iy, flag):     # count 인자 추가
    global cnt
    visited[board[ix][iy]] = True
 
    if flag == 1:
        for k in range(len(nxt1)):
            # 다음 index
            idx1, idx2 = ix + nxt1[k][0], iy + nxt1[k][1]
            if 0 <= idx1 < N and 0 < idx2 < N:    # 범위를 벗어나지 않았다면
                if visited[board[idx1][idx2]] == False:    # 중복값이 아니면
                    if k == 1:                        
                        flag = 2
                    move(idx1, idx2, flag)
                    visited[board[idx1][idx2]] = False
 
    elif flag == 2:
        for k in range(len(nxt2)):
            idx1, idx2 = ix + nxt2[k][0], iy + nxt2[k][1]
            if 0 < idx1 < N and 0 <= idx2 < N:
                if visited[board[idx1][idx2]] == False:
                    if k == 1:
                        flag = 3
                    move(idx1, idx2, flag)
                    visited[board[idx1][idx2]] = False
 
    elif flag == 3:
        if ix-i == j-iy:
            flag = 4
            idx1, idx2 = ix-1, iy+1
            if 0 <= idx1 < N and 0 <= idx2 < N:
                if idx1 == i and idx2 == j:
                    cnt.append(visited.count(True))
                elif visited[board[idx1][idx2]] == False:
                    move(idx1, idx2, flag)
                    visited[board[idx1][idx2]] = False
        else:
            idx1, idx2 = ix-1, iy-1
            if 0 <= idx1 < N and 0 <= idx2 < N:
                if visited[board[idx1][idx2]] == False:
                    move(idx1, idx2, flag)
                    visited[board[idx1][idx2]] = False
         
    elif flag == 4:
        idx1, idx2 = ix-1, iy+1
        if 0 <= idx1 < N and 0 <= idx2 < N:
            if idx1 == i and idx2 == j:
                cnt.append(visited.count(True))
            elif visited[board[idx1][idx2]] == False:
                move(idx1, idx2, flag)
                visited[board[idx1][idx2]] = False
 
 
 
 
# main

# dx, dy
nxt1 = [(1, 1), (1, -1)]
nxt2 = [(1, -1), (-1, -1)]
 
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    # start index
    cnt = []
    for i in range(N-2):
        for j in range(1, N-1):
            # initial settings
            flag = 1
            visited = [False for i in range(101)]
            move(i, j, flag)
    if len(cnt) != 0:
        print(f'#{tc} {max(cnt)}')
    else:
        print(f'#{tc} -1')