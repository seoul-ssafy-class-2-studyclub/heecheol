import sys
sys.stdin = open('input.txt', 'r')


def work(k, arr=[]):
    global max_money

    if k > N:
        arr.pop()
        if max_money < sum(arr):
            max_money = sum(arr)
        return

    elif k == N:
        if max_money < sum(arr):
            max_money = sum(arr)
        return

    else:
        for i in range(k, N):
            work(i + T[i], arr + [P[i]])


N = int(input())
T = [0] * N
P = [0] * N

for i in range(N):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

max_money = 0
work(0)
print(max_money)
