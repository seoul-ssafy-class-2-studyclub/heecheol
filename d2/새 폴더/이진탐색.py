
def count(l, r, page):
    c = int((l + r)/2)
    if c == page:
        cnt = 0
        return cnt
    else:
        if page > c:
            l = c
            return count(l, r, page) + 1  
        else:
            r = c
            count(l, r, page)
            return count(l, r, page) + 1

for T in range(1, int(input()) + 1):
    P, Pa, Pb = map(int, input().split())

    A = count(1, P, Pa)
    B = count(1, P, Pb)

    if A > B:
        print(f'#{T} B')
    elif B > A:
        print(f'#{T} A')
    else:
        print(f'#{T} 0')
    
