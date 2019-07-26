# 3,6,9 게임

N = int(input())

for number in range(1, N + 1):
    
    num = str(number)   # int to string

    clap_num = ('3', '6', '9')
    clap = 0

    for i in num:
        if i in clap_num:
            clap += 1
        else:
            pass
    if clap == 0:
        print(number, end=' ')
    else:
        print('-' * clap, end=' ')

'''
N = int(input())

for number in range(1, N + 1):  
    
    num = list(str(number))
    num = list(map(int, num))   # int => str => int (seperated int list)

    clap_num = (3, 6, 9)
    clap = 0

    for i in range(len(num)):   
        if num[i] in clap_num:
            clap += 1
        else:
            pass
    if clap == 0:
        print(number, end=' ')
    else:
        print('-' * clap, end=' ')
'''