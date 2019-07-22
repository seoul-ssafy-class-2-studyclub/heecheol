# 기차 사이의 파리

t = int(input())

for i in range(t):
    D, A, B, F = map(int, input().split())

    hour = []
    h = 0
    while D > 0.0000000001:
        h = D / (F + B)
        hour.append(h)
        D = (F - A) * h

        h = D / (F + A)
        D = (F - B) * h
        hour.append(h)
flyfly = sum(hour) * F
print(f'#{i + 1} {flyfly}')