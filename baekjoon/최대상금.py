import sys
sys.stdin = open('input.txt', 'r')


def prize_list(str_num, cnt):
    global result

    if cnt == M:
        if result < str_num:
            result = str_num
        return

    else:
        num = list(str_num)
        dp = []
        for i in range(length - 1):
            for j in range(i+1, length):
                num[i], num[j] = num[j], num[i]
                prize = ''.join(num)
                if prize not in dp:
                    # print(prize)
                    dp.append(prize)
                    prize_list(prize, cnt + 1)
                num[i], num[j] = num[j], num[i]


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    result = '0'
    length = len(str(N))
    prize_list(str(N), 0)
    print('#{} {}'.format(tc, result))