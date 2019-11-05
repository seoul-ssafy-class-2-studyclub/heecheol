import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    node, edge = map(int, input().split())
    arr = [[] for i in range((node+1))]

    for e in range(edge):
        num1, num2 = map(int, input().split())
        arr[num1].append(num2)

    start_point, end_point = map(int, input().split())

    visited = [False] * (node+1)    
    visited[start_point] = True

    stack = []
    stack += arr[start_point]

    while len(stack):
        i = stack.pop()
        if i == end_point:
            print('#{} 1'.format(tc+1))
            break
        if visited[i] == False:
            visited[i] = True
            stack += arr[i]
    else:
        print('#{} 0'.format(tc+1))
        
