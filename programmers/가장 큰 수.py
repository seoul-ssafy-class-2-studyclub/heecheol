def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)

    N = len(numbers)

    for i in range(1, N):
        if len(numbers[i]) == len(numbers[i-1]):
            continue
        else:
            for j in range(i, 0, -1):
                if numbers[j-1]+numbers[j] >= numbers[j]+numbers[j-1]:
                    break
                else:
                    numbers[j], numbers[j-1] = numbers[j-1], numbers[j]

    answer = str(int(''.join(numbers)))

    return answer


print(solution([3, 30, 34, 5, 9]))
