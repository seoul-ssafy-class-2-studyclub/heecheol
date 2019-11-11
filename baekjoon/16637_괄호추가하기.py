import sys
sys.stdin = open('input.txt', 'r')


def combination(idx, arr):
    if idx > N - 2:
        calc_list.append(arr)
        return
    else:
        combination(idx + 2, arr)
        combination(idx + 4, arr + [idx])


N = int(input())
calc = list(input())
calc_list = []
combination(1, [])
result = -2 ** 31

for c_list in calc_list:
    new_calc = calc[:]
    for _ in range(len(c_list)):
        c = c_list.pop()
        if new_calc[c] == '+':
            new_calc[c - 1:c + 2] = [int(new_calc[c - 1]) + int(new_calc[c + 1])]
        elif new_calc[c] == '-':
            new_calc[c - 1:c + 2] = [int(new_calc[c - 1]) - int(new_calc[c + 1])]
        else:
            new_calc[c - 1:c + 2] = [int(new_calc[c - 1]) * int(new_calc[c + 1])]

    temp = int(new_calc[0])
    for i in range(len(new_calc) // 2):
        operator = new_calc[2 * i + 1]
        if operator == '+':
            temp += int(new_calc[2 * (i + 1)])
        elif operator == '-':
            temp -= int(new_calc[2 * (i + 1)])
        else:
            temp *= int(new_calc[2 * (i + 1)])
    if 2 ** 31 > temp > result:
        result = temp

print(result)
