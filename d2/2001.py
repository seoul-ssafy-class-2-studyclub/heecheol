# 파리퇴치

for t in range(int(input())):
        
    N, M = map(int, input().split())
    num_list = []
    
    for o in range(N):
        num_list.append(list(map(int, input().split())))

    max_kill = 0
    position = N - M + 1
    
    for i in range(position):
        for j in range(position):
            square = 0 
            for a in range(M):
                for b in range(M):
                    square += num_list[i + a][j + b]
            if square >= max_kill:
                max_kill = square

    print(f'#{t + 1} {max_kill}')
