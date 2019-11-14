import itertools
import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

max_money = 0

for num in range(N + 1):
    arr_list = list(itertools.combinations(list(range(N)), num))
    for arr in arr_list:
        flag = True
        for i in range(num):
            if i == num - 1:
                if arr[i] + T[arr[i]] > N:
                    flag = False
                    break

            elif arr[i] + T[arr[i]] > N:
                flag = False
                break

            elif arr[i] + T[arr[i]] > arr[i + 1]:
                flag = False
                break

        if flag is True:
            money = 0
            for i in range(num):
                money += P[arr[i]]
            if max_money < money:
                max_money = money

print(max_money)
