# 몫과 나머지 출력하기
tries = int(input())
for i in range(1, tries + 1):
    num = list(map(int, input().split()))
    a, b = divmod(num[0], num[1])
    print(f'#{i} {a} {b}')
