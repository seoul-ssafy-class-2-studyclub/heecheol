def solution(food_times, k):
    time = 0

    n = len(food_times)

    total = sum(food_times)
    if k >= total:
        return -1

    min_time = min(food_times) - 1
    if min_time * n < k:
        for food in food_times:
            food -= min_time
        k -= min_time * n

    before = [n - 1] + list(range(n - 1))
    after = list(range(1, n)) + [0]
    idx = 0

    while time < k:
        if food_times[idx] > 1:
            food_times[idx] -= 1

        else:
            food_times[idx] = 0
            after[before[idx]] = after[idx]
            before[after[idx]] = before[idx]

        idx = after[idx]
        time += 1

    return idx + 1


solution([3, 1, 2], 5)
