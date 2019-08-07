def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


for T in range(10):
    N = int(input())
    matrix = []
    sum_max = 0
    for i in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
        if sum_max < sum(row):
            sum_max = sum(row)

    l_cross = []
    r_cross = []
    matrix = list(zip(*matrix))
    for i in range(100):
        if sum_max < sum(matrix[i]):
            sum_max = sum(matrix[i])
        l_cross.append(matrix[i][i])
        r_cross.append(matrix[i][-1-i])

    sum_max = max([sum_max, sum(l_cross), sum(r_cross)])

    print(f'#{N} {sum_max}')

