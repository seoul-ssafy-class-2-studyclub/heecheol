numbers = []
for tc in range(int(input())):
    N = int(input())
    numbers.append(N)

primes = []

for number in range(2, max(numbers)):
    for n in range(2, number//2+1):
        if number % n == 0:
            break
    else:
        primes.append(number)
print(primes)
tc = 1
for number in numbers:
    cnt = 0
    for a in range(len(primes)):
        for b in range(a, len(primes)):
            for c in range(b, len(primes)):
                if primes[a] + primes[b] + primes[c] == number:
                    cnt += 1
                    break
                elif primes[a] + primes[b] + primes[c] > number:
                    break
                
    print(f'{tc} {cnt}')
    tc += 1