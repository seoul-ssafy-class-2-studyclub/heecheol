import sys
sys.stdin = open('input.txt', 'r')


def int_two(nums):
    int_num = 0
    for i in range(len(nums)):
        int_num = int_num*2 + nums[i]
    return int_num


def int_three(nums):
    int_num = 0
    for i in range(len(nums)):
        int_num = int_num*3 + nums[i]
    return int_num


for tc in range(1, int(input())+1):
    two = list(map(int, list(input())))
    three = list(map(int, list(input())))

    two_list = []
    for i in range(len(two)):
        if two[i] == 0:
            two[i] = 1
            two_list.append(int_two(two))
            two[i] = 0
        else:
            two[i] = 0
            two_list.append(int_two(two))
            two[i] = 1

    three_list = []
    for i in range(len(three)):
        if three[i] == 0:
            three[i] = 1
            three_list.append(int_three(three))
            three[i] = 2
            three_list.append(int_three(three))
            three[i] = 0
        elif three[i] == 1:
            three[i] = 0
            three_list.append(int_three(three))
            three[i] = 2
            three_list.append(int_three(three))
            three[i] = 1
        else:
            three[i] = 0
            three_list.append(int_three(three))
            three[i] = 1
            three_list.append(int_three(three))
            three[i] = 2

    # print(two_list)
    # print(three_list)

    for number in two_list:
        if number in three_list:
            print('#{} {}'.format(tc, number))
            break