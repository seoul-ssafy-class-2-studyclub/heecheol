import re


def solution(user_id, banned_id):

    user_number = {}
    for i in range(len(user_id)):
        user_number[user_id[i]] = str(i)

    banned_list = ['' for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        ban = banned_id[i].replace('*', '.')
        pat = re.compile(ban)
        for j in range(len(user_id)):
            if pat.match(user_id[j]) and len(ban) == len(user_id[j]):
                banned_list[i] += str(j)

    banned_list.sort(key=lambda x: len(x))

    result = set()

    def recursion(arr, k):
        if k == len(banned_list):
            temp = sorted(arr)
            result.add(''.join(temp))
            return
        else:
            for n in banned_list[k]:
                if n not in arr:
                    recursion(arr+[n], k+1)

    recursion([], 0)

    answer = len(result)
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
