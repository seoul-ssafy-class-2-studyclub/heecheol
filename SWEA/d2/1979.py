test = int(input())
for t in range(test):
    N, K = map(int, input().split())
    num = []
    blank = 0
    count = 0

    for i in range(N):
        num.append(input().split())

    for i in range(N):
        blank = 0
        for j in range(N):
            if num[i][j] == '1':
                blank += 1
                if blank == K:
                    count += 1
                elif blank == K + 1:
                    count -= 1
                    blank = 0
            else:
                blank = 0

    for i in range(N):
        blank = 0
        for j in range(N):
            if num[j][i] == '1':
                blank += 1
                if blank == K:
                    count += 1
                elif blank == K + 1:
                    count -= 1
                    blank = 0
            else:
                blank = 0


    print(f'#{t + 1} {count}')

