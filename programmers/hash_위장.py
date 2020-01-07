import itertools


def solution(clothes):

    data = {}
    for i in range(len(clothes)):
        cloth_name, cloth_type = clothes[i]

        if cloth_type in data:
            data[cloth_type] += 1
        else:
            data[cloth_type] = 1

    answer = 0
    counts = list(data.values())
    counts.sort()

    for n in range(1, len(counts) + 1):
        combs = list(itertools.combinations(counts, n))
        dp = {}
        for comb in combs:
            key = ''.join(list(map(str, list(comb))))

            if key in dp:
                answer += dp[key]

            else:
                temp = 1
                for num in list(comb):
                    temp *= num
                answer += temp
                dp[key] = temp

    return answer


arr = []
print(solution(arr))
