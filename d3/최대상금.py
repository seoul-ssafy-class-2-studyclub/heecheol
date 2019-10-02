import sys
sys.stdin = open('input.txt', 'r')


def prize_list(str_num, cnt):
    global s
    global result
    global flag

    # if str_num == sorted_num:
    #     if (M - cnt) % 2 == 0:
    #         result = str_num
    #         return False
    #     elif M - cnt > 0 and (M - cnt) % 2 == 0:
    #         result = str_num
    #         return False

    if cnt == M:
        # print(str_num)
        if sorted_num == str_num:
            result = str_num
            return False
        elif result < str_num:
            result = str_num
        return True

    else:
        for a in range(length - 2):
            if str_num[a] != sorted_num[a]:
                break
            else:
                if a == length - 2:
                    result = str_num
                    return False
                elif s < a:
                    s = a
        num = list(str_num)
        dp = []
        for i in range(s, length - 1):
            for j in range(i+1, length):
                num[i], num[j] = num[j], num[i]
                prize = ''.join(num)

                if prize not in dp:
                    dp.append(prize)
                    flag = prize_list(prize, cnt + 1)
                    if flag is False:
                        return False
                num[i], num[j] = num[j], num[i]


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    result = '0'
    flag = True
    length = len(str(N))
    s = 0
    sorted_num = ''.join(sorted(list(str(N)), reverse=True))
    # print(sorted_num)
    prize_list(str(N), 0)
    print('#{} {}'.format(tc, result))