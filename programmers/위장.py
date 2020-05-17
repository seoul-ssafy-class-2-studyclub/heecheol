def solution(clothes):
    import collections

    count = collections.defaultdict(int)
    for i in range(len(clothes)):
        name, category = clothes[i]
        count[category] += 1

    answer = 1
    for key, value in count.items():
        answer *= (value + 1)

    return answer - 1


solution([['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']])