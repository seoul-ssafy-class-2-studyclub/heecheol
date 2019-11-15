import sys
sys.stdin = open('input.txt', 'r')


def permutations(k, arr):
    if k == N - 1:
        operators.append(arr)
        return
    else:
        for i in range(4):
            if op_input[i] > 0:
                op_input[i] -= 1
                permutations(k + 1, arr + [i])
                op_input[i] += 1


N = int(input())
numbers = list(map(int, input().split()))
op_input = list(map(int, input().split()))

operators = []
permutations(0, [])

max_value = -1000000000
min_value = 1000000000

for operator in operators:
    total = numbers[0]

    for i in range(N - 1):
        op = operator[i]
        if op == 0:
            total += numbers[i + 1]
        elif op == 1:
            total -= numbers[i + 1]
        elif op == 2:
            total *= numbers[i + 1]
        else:
            total = int(total / numbers[i + 1])

    if total > max_value:
        max_value = total
    if total < min_value:
        min_value = total

print(max_value)
print(min_value)
