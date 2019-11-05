# t = int(input())
# for i in range(1, t + 1):
#     N = int(input())
#     a = b = c = d = e = 0
    
#     while N != 1:
#         if N % 2 == 0:
#             N = N // 2
#             a += 1

#         if N % 3 == 0:
#             N = N // 3
#             b += 1
            
#         if N % 5 == 0:
#             N = N // 5
#             c += 1
            
#         if N % 7 == 0:
#             N = N // 7
#             d += 1
            
#         if N % 11 == 0:
#             N = N // 11
#             e += 1

#     print(f'#{i} {a} {b} {c} {d} {e}')
    
t = int(input())

for i in range(1, t + 1):
    n = int(input())
    t = []  # list
    for j in (2, 3, 5, 7, 11):  # tuple
        k = 0
        while n % j == 0:   
            n /= j
            k += 1
        t.append(str(k))
    re = ' '.join(t)
    print(f'#{i}', re)