def pattern(string_list):
    set_list = list(set(string_list))
    
    for length in range(len(set_list), 11):
        if 4 <= length <= 10:
            check_list = string_list[0: length]
            check_range = string_list[0: length * 3]
            if check_list * 3 == check_range:
                return length
        else:
            check_list = string_list[0: length]
            check_range = string_list[0: length * 6]
            if check_list * 6 == check_range:
                return length
    else:
        return '문자열이 올바르지 않습니다.'

for i in range(int(input())):
    str_list = list(input())

    if len(str_list) == 30:
        pattern_len = pattern(str_list)
        print(pattern_len)
    else:
        print('입력이 30개가 아닙니다.')
