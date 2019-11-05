import sys
sys.stdin = open('input.txt', 'r')


def move(ix, iy):
    global flag     
    global cnt   
    
    if flag == 1:   #
        for n in range(len(nxt1)):     # flag 1 유지, 2로 변경
            idx1, idx2 = ix+nxt1[n][0], iy+nxt1[n][1]
            if 0 <= idx1 < N-1 and 0 <= idx2 < N:
                if visited[board[idx1][idx2]] == False:
                    visited[board[idx1][idx2]] = True
                    if n == 1:
                        flag = 2
                    print(f'# {idx1}, {idx2} flag_ {flag}')
                    move(idx1, idx2)
                    visited[board[idx1][idx2]] = False
    elif flag == 2:
        for n in range(len(nxt2)):
            idx1, idx2 = ix+nxt2[n][0], iy+nxt2[n][1]
            if 0 <= idx1 < N and 0 <= idx2 < N:
                if visited[board[idx1][idx2]] == False:
                    visited[board[idx1][idx2]] = True
                    if n == 1:
                        flag = 3
                    print(f'# {idx1}, {idx2} flag_ {flag}')
                    move(idx1, idx2)
                    visited[board[idx1][idx2]] = False
    elif flag == 3:
        if ix-i == j-iy:
            flag = 4
            idx1, idx2 = ix-1, iy+1
            print(f'# {idx1}, {idx2} flag_ {flag}')
            if 0 <= idx1 < N and 0 <= idx2 < N: # del
                if idx1 == i and idx2 == j:
                    if visited[board[idx1][idx2]] == False:
                        visited[board[idx1][idx2]] = True     
                        cnt = visited.count(True)
                        print(f'result is {cnt}')
                elif visited[board[idx1][idx2]] == False:
                    visited[board[idx1][idx2]] = True
                    move(idx1, idx2)
                    visited[board[idx1][idx2]] = False
        else:
            idx1, idx2 = ix-1, iy-1
            print(f'# {idx1}, {idx2} flag_ {flag}')
            if 0 <= idx1 < N and 0 <= idx2 < N:
                if visited[board[idx1][idx2]] == False:
                    visited[board[idx1][idx2]] = True
                    move(idx1, idx2)
                    visited[board[idx1][idx2]] = False
    elif flag == 4:
        print(i, j)
        idx1, idx2 = ix-1, iy+1
        print(f'# {idx1}, {idx2} flag_ {flag}')
        if idx1 == i and idx2 == j:
            if visited[board[idx1][idx2]] == False:
                visited[board[idx1][idx2]] = True     
                cnt = visited.count(True)
                print(f'result is {cnt}')
        else:
            if 0 <= idx1 < N and 0 <= idx2 < N:
                if visited[board[idx1][idx2]] == False:
                    visited[board[idx1][idx2]] = True
                    move(idx1, idx2)
                    visited[board[idx1][idx2]] = False




TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    nxt1 = [(1, 1), (1, -1)]
    nxt2 = [(1, -1), (-1, -1)]
    nxt3 = [(-1, -1), (-1, 1)]

    for i in range(N-2):
        for j in range(1, N-1):
            flag = 1
            visited = [False for i in range(101)]
            max_distance = -1
            cnt = 0
            print(f'start {i}, {j}')
            move(i, j)