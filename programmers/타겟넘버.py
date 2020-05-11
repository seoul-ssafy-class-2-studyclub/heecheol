def solution(numbers, target):
    from collections import defaultdict

    n = len(numbers)

    counts = [defaultdict(int) for _ in range(n + 1)]
    counts[0] = {0: 1}

    for i in range(n):
        number = numbers[i]
        for key, value in counts[i].items():
            counts[i + 1][key + number] += value
            counts[i + 1][key - number] += value

    # print(counts[-1][target])
    answer = counts[-1][target]

    return answer


solution([1, 1, 1, 1, 1], 3)
