def find_maximum(list1, list2):
    result = 0
    tries = len(list1) - len(list2)     # 두 리스트의 길이 차이
    for j in range(tries + 1):          # list2가 한 칸씩 어디까지 움직이는지 
        maximum = 0
        for i in range(len(list2)):     
            maximum += list1[i + j] * list2[i]
            
        if maximum > result:
            result = maximum
            
    return result




T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    A = list(map(int, input().split())) 
    B = list(map(int, input().split()))

    # 함수에서 인자를 받을 때 len(list1) >= len(list2) 로 받기위해
    if N >= M:  
        max = find_maximum(A, B)
    else:
        max = find_maximum(B, A)
    
    print(f'#{t} {max}')