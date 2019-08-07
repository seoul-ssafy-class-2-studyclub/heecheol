A = []
for i in range(1, 13):
    A.append(i)

for tc in range(int(input())):
    N, K = map(int, input().split())

    cnt = 0
    for i in range(1<<12):
        subset = []
        
        for j in range(12):
            if i & (1<<j):
                num = A[j]
                subset.append(num)
                
        if len(subset) == N and sum(subset) == K:
            cnt += 1
    print(f'#{tc+1} {cnt}')
            
