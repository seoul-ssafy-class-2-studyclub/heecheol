def solution(prices):
    n = len(prices)
    answer = list(range(n-1, -1, -1))

    stack = [(prices[0], 0)]
    for i in range(1, n):
        while stack:
            if stack[-1][0] > prices[i]:
                a, b = stack.pop()
                answer[b] = i-b
            else:
                break
        stack.append((prices[i], i))

    return answer


print(solution([1, 2, 3, 2, 3, 1]))
