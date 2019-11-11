def solution(user_id, banned_id):
    import itertools
    banned_num = len(banned_id)
    total = list(itertools.combinations(user_id, banned_num))

    answer = 0
    for users in total:
        perm_users = list(itertools.permutations(users, banned_num))
        flag1 = True
        for perm_user in perm_users:
            flag2 = True
            for i in range(banned_num):
                user = perm_user[i]
                ban = banned_id[i]

                if len(user) != len(ban):
                    flag2 = False
                    break
                else:
                    for j in range(len(user)):
                        if ban[j] == '*':
                            continue
                        elif user[j] == ban[j]:
                            continue
                        else:
                            flag2 = False
                            break

                if flag2 is False:
                    break
            if flag2 is True:
                answer += 1
                break
    print(answer)
    return answer

user_id_input = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id_input = ["fr*d*", "*rodo", "******", "******"]
solution(user_id_input, banned_id_input)