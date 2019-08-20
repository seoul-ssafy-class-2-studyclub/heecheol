import sys
sys.stdin = open('input.txt', 'r')

visit = [True] * 100
stack = [0] * 200

tc, N = map(int, input().split())
data = list(map(int, input().split()))

arr1 = [0] * 100
arr2 = [0] * 100

for n in range(N):
    i = data[2*n]
    if arr1[i] == 0:
        arr1[i] = data[2*n+1]
    else:
        arr2[i] = data[2*n+1]

top = 0
stack[top] = arr1[0]
if arr2[0] != 0:
    stack[top+1] = arr2[0]
    top += 1
 
while stack[0] != 0:
    i = stack[top]
    stack[top] = 0
    top -= 1

    if visit[i] == True and arr1[i] != 0:
        visit[i] = False
        stack[top+1] = arr1[i]
        top += 1
        if arr2[i] != 0:
            stack[top+1] = arr2[i]
            top += 1
        
    
