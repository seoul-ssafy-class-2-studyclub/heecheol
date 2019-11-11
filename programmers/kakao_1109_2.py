def solution(s):
    arr = []
    for i in range(1, len(s) - 1):
        if s[i] == '{':
            tup = []
            continue
        elif s[i] == '}':
            arr.append(''.join(tup).split(','))
            # arr.append(''.join(tup).split(','))
            continue
        else:
            tup.append(s[i])
    print(arr)
    # dict = {}
    # for part in arr:
    #     dict[len(part)] = set(part)
    # answer = list(dict[1])
    # for i in range(1, len(arr)):
    #     answer += list(dict[i + 1] - dict[i])
    # answer = list(map(int, answer))

    # return answer

ss = "{{20,111},{111}}"
solution(ss)