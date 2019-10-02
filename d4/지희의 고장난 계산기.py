import sys
sys.stdin = open('input.txt', 'r')


def search(n, k, str_num):
    # 총 n자리, 현재 k자리
    if n == k:
        if str_num[0] == '0':
            return
        elif num_X < int(str_num):
            return
        else:
            if num_X % int(str_num):
                return
            else:
                our_num.append(int(str_num))
                touch.append(len(str_num))
                return
    else:
        for nxt in key_num:
            search(n, k + 1, str_num + nxt)
            # if search(n, k + 1, str_num + nxt) is False:
    #             #     return False


def division(cur_num, cnt):
    global min_cnt
    if cur_num == 1:
        if cnt < min_cnt:
            min_cnt = cnt
        return
    else:
        for i in range(len(our_num)):
            if cur_num % our_num[i] == 0:
                division(cur_num // our_num[i], cnt + touch[i] + 1)


for tc in range(1, int(input()) + 1):
    data = list(map(int, input().split()))

    # 누를 수 있는 숫자, type: str
    key_num = []
    for i in range(10):
        if data[i]:
            key_num.append(str(i))

    # 목표 숫자
    num_X = int(input())

    # 만들 수 있는 숫자 중에 나누어 떨어지는 숫자 리스트, type: int
    our_num = []
    touch = []
    for i in range(1, len(str(num_X)) + 1):
        search(i, 0, '')

    if our_num:
        if num_X in our_num:
            print('#{} {}'.format(tc, len(str(num_X)) + 1))
        else:
            if our_num[0] == 1 and num_X != 1:
                our_num.pop(0)
                touch.pop(0)

            min_cnt = 987654321
            # print(our_num)
            # print(touch)

            if our_num:
                division(num_X, 0)
                if min_cnt == 987654321:
                    print('#{} -1'.format(tc))
                else:
                    print('#{} {}'.format(tc, min_cnt))
            else:
                print('#{} -1'.format(tc))
    else:
        print('#{} -1'.format(tc))