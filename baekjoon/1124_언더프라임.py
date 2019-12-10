import sys
sys.stdin = open('input.txt', 'r')


def factorization(n):
    k = 0
    cnt = 0
    while n != 1:
        if n % prime_nums[k] == 0:
            n //= prime_nums[k]
            cnt += 1
        else:
            k += 1

    return cnt


A, B = map(int, input().split())
primes = [False, False] + [True] * (B - 1)
prime_nums = []
for i in range(2, B + 1):
    if primes[i] is True:
        j = 2
        while i * j <= B:
            primes[i * j] = False
            j += 1
        prime_nums.append(i)

result = 0
for num in range(A, B + 1):
    if primes[factorization(num)] is True:
        result += 1

# print(primes)
print(result)
