# 기차 사이의 파리

t = int(input())

for i in range(t):
    D, A, B, F = map(int, input().split())

    hour = []                   # list of hours fly flies
    h = 0

    while D > 0.00000001:       # until train collide
        h = D / (F + B)         # hour fly => B
        D = (F - A) * h         # distance between A and fly when fly at B
        hour.append(h)
        

        h = D / (F + A)         # hour fly => A
        D = (F - B) * h         # distance between A and fly when fly at B
        hour.append(h)

flyfly = sum(hour) * F          # total distance is velocity * hours
print(f'#{i + 1} {flyfly}')