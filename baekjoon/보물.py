import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

A_arr.sort()
B_arr.sort(reverse=True)

total = 0
for i in range(N):
    total += A_arr[i] * B_arr[i]

print(total)