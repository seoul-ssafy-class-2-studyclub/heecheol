
# t = int(input())

# for i in range(t):
#     D, A, B, F = map(int, input().split())
#     hour = D / (A + B)
#     flyfly = F * hour

#     print(f'#{i + 1} {flyfly}')


t = int(input())

for i in range(t):
    D, A, B, F = map(int, input().split())

    hour = []
    h = 0
    while D > 0.0000001:
        h = D / (F + B)
        hour.append(h)
        D = (F - A) * h

        h = D / (F + A)
        D = (F - B) * h
        hour.append(h)

print(sum(hour))

# T = int(input())
# for t in range(1, T + 1):
#     d, a, b, f = map(int, input().split())
#     time = d / (a + b)
#     distance = time * f
#     print(f'#{t} {distance:.7f}')
