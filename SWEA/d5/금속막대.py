import sys
sys.stdin = open('input.txt', 'r')

def connect(nut, arr):
    for i in range(len(arr)):
        if nut == arr[i][0]:
            nut = arr[i][1]
            new_arr.append(arr.pop(i))
            connect(nut, arr)
            return 0
    else: 
        return 0

for tc in range(int(input())):

    N = int(input())
    inputs = list(map(int, input().split()))
    long_arr = []

    arr2 = []
    for j in range(N):
            one = []
            one.append(inputs[2*j])
            one.append(inputs[2*j + 1])
            arr2.append(one)

    for i in range(N):
        arr = arr2[:]
        new_arr = []                        
        nut = arr[i][1]
        new_arr.append(arr.pop(i))
        if connect(nut, arr) == 0 and len(new_arr) > len(long_arr):
            long_arr = new_arr

    print(long_arr)
    result = ''
    for i in range(len(long_arr)):
        for j in range(2):
            result += str(long_arr[i][j]) + ' '
            
    print('#{} {}'.format(tc+1, result))