import sys
sys.stdin = open('input.txt', 'r')


def binary_search(left, right, num):
    if left == right:
        if num < result[left]:
            result[left] = num
        return
    else:
        middle = (left + right) // 2

        if num < result[middle]:
            binary_search(left, middle, num)

        elif num == result[middle]:
            return

        else:
            binary_search(middle + 1, right, num)


N = int(input())
numbers = list(map(int, input().split()))
result = [numbers[0]] + [0] * N
end = 0

for i in range(1, N):
    if numbers[i] > result[end]:
        end += 1
        result[end] = numbers[i]

    elif numbers[i] == result[end]:
        continue

    else:
        binary_search(0, end, numbers[i])

print(end + 1)
