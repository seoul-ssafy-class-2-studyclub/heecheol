import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
odd = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
even = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for n in range(1, N):
    if n % 2:
        for i in range(10):
            even[i] = odd[i - 1] + odd[i + 1]
    else:
        for i in range(10):
            odd[i] = even[i - 1] + even[i + 1]

if N % 2:
    print(sum(odd) % 1000000000)
else:
    print(sum(even) % 1000000000)
