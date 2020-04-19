# programmers
# stack/queue


def solution(heights):
    n = len(heights)
    answer = [0] * n
    high = 0

    for i in range(n):
        if heights[i] >= high:
            high = heights[i]
        else:
            k = i - 1
            while k >= 0:
                if heights[k] > heights[i]:
                    answer[i] = k + 1
                    break
                k -= 1

    return answer


h = [3, 9, 9, 3, 5, 7, 2]
solution(h)