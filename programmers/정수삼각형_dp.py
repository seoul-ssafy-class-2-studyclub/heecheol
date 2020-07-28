def solution(triangle):

    N = len(triangle)
    for r in range(N):
        triangle[r].append(0)

    for i in range(1, N):
        for j in range(i+1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

    answer = max(triangle[-1])

    return answer


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
