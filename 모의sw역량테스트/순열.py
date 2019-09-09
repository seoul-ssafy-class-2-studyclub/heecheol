import itertools

# 1부터 N까지의 수를 배열하는 코드

def perm(n, k):
    
    if n == k:
        print(a)

    else:
        for i in range(k, n):
            a[k], a[i] = a[i], a[k]
            perm(n, k+1)
            a[k], a[i] = a[i], a[k]

N = 5
a = [3, 6, 8, 9, 7]
# perm(N, 0)

# result = itertools.permutations(a)


result = itertools.combinations(a, 4)
print(list(result))