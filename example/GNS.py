import sys
sys.stdin = open('input.txt', 'r')

nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

def atoi(num):
    if num == 'ZRO':
        return 0
    elif num == 'ONE':
        return 1
    elif num == 'TWO':
        return 2
    elif num == 'THR':
        return 3
    elif num == 'FOR':
        return 4
    elif num == 'FIV':
        return 5
    elif num == 'SIX':
        return 6
    elif num == 'SVN':
        return 7
    elif num == 'EGT':
        return 8
    elif num == 'NIN':
        return 9
    else:
        print('wrong input')


for n in range(int(input())):
    # counting sort
    tc, size = input().split()
    size = int(size)

    data = input().split()


    count = [0] * 10
