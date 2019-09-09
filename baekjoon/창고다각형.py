import sys
sys.stdin = open('input.txt', 'r')

arr = [0] * 1000
N = int(input())
l_max = 0
h_max = 0

for n in range(N):
    L, H = map(int, input().split())
    arr[L] = H
    if H > h_max:
        h_max = H
        l_max = L

height = 0
j = 0
total = 0

for i in range(l_max + 1):
    if arr[i] > height:
        height = arr[i]
    else:
        arr[i] = height

        
height = 0
j = 999
for i in range(999, l_max - 1, -1):
    if arr[i] > height:
        height = arr[i]
    else:
        arr[i] = height
                
print(sum(arr))
