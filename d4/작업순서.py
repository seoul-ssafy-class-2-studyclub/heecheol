import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 11):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))

    arr1 = [[] for i in range(V+1)]
    arr2 = [[] for i in range(V+1)]
    visited = [False for i in range(V+1)]

    for e in range(E):
        # 
        node = data[2*e]
        next_node = data[2*e+1]
        
        # arr1 은 진출노드 리스트
        arr1[node] += [next_node]
        # arr2 는 진입노드 리스트
        arr2[next_node] += [node]
        
    result = []

    while True:
        stack1 = []
        stack2 = []
        for i in range(1, V+1):
            if visited[i] == False and len(arr2[i]) == 0:
                stack1 += arr1[i]
                stack2.append(i)
                visited[i] = True
        
        if len(stack2) == 0:
            break
        else:
            result += stack2

        for a in stack1:
            for b in stack2:
                if b in arr2[a]:
                    arr2[a].remove(b)
        
    
    reresult = ' '.join(list(map(str, result)))
    
    print(f'#{tc} {reresult}')
