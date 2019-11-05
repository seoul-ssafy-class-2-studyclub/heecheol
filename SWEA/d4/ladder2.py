from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')

for tc in range(10):
    N = int(input())
    ladder = [] 
    for row in range(100):
        ladder.append(input().split())
    
    start_cols = []
    for i in range(100):
        if ladder[0][i] == '1':
            start_cols.append(i)

    shortest = 10000
    start_point = 0
    
    for start_col in start_cols:
        row = 0
        flag = 0
        cnt = 0
        col = start_col        
    
        while row < 99:
            if flag == 0:
                if col != 99 and ladder[row][col+1] == '1':
                    col += 1
                    cnt += 1
                    flag = 1
                elif col != 0 and ladder[row][col-1] == '1':
                    col -= 1
                    cnt += 1
                    flag = 2
                else:
                    row += 1
            elif flag == 1:
                if ladder[row+1][col] == '1':
                    row += 1
                    flag = 0
                else:
                    col += 1
                    cnt += 1
            else:
                if ladder[row+1][col] == '1':
                    row += 1
                    flag = 0
                else:
                    col -= 1
                    cnt += 1

            if cnt > shortest:
                break

        if cnt <= shortest:
            shortest = cnt
            start_point = start_col
            
    print(f'#{N} {start_point}')
    