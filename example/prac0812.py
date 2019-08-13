# Palindrome

# string = list(input())

# for i in range(len(string)//2):
#     if string[i] != string[-i-1]:
#         print('is_not_palindrome')
#         break
# else:
#     print('palindrome')


# itoa()


# def itoa(num):
#     if num == 0:
#         return str_num
#     else:
#         a= chr(num % 10 + ord('0'))
#         str_num.append(a)       
#     return itoa(num//10)

# str_num = []
# print(itoa(1234))


def itoa(x):
    sr = ''
    while True:
        r = x % 10
        sr = sr + chr(r + ord('0'))
        x //= 10
        if x == 0:
            break
    s = ''
    print(type(sr))
    for i in range(len(sr)-1, -1, -1):
        s = s + sr[i]
    return s

print(itoa(1234))

