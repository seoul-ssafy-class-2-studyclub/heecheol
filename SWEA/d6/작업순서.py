import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1):
    V, E = map(int, input().split())
    data = list(map(int, input().split()))

    arr1 = [[] for i in range(V+1)]    # 진출
    arr2 = [[] for i in range(V+1)]    # 진입
    visited = [False for i in range(V+1)]
    stack = []

    for e in range(E):
        arr1[data[2*e]] += [data[2*e+1]]
        arr2[data[2*e+1]] += [data[2*e]]
        visited[data[2*e]] = True
        
    print(arr1)
    print(arr2)
    
    