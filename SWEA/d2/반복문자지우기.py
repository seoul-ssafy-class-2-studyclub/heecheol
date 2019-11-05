import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    origin_str = list(input())
    print(origin_str)

    while True:
        count = 0
        for i in range(1, len(origin_str)):
            if origin_str[i] == origin_str[i-1]:
                origin_str[i-1] = '_'
                origin_str[i] = '_'
                count += 2
        if count == 0:
            break
        for i in range(count):
            origin_str.remove('_')
    
    print('#{} {}'.format(tc+1, len(origin_str)))


        