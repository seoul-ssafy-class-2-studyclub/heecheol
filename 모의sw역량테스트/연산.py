import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    numbers = [N]
    cnt = 0
    flag = True
    while True:
        cnt += 1
        LEN = len(numbers)
        for _ in range(LEN):
            num = numbers.pop(0)
            arr = []

            p = num + 1
            if p <= 1000000:
                arr.append(p)

            mt = num * 2
            if mt <= 1000000:
                arr.append(mt)

            m = num - 1
            if m > 0:
                arr.append(m)

            m_ten = num - 10
            if m_ten > 0:
                arr.append(m_ten)

            if M in arr:
                flag = False
                break
            else:
                numbers.extend(arr)

        if flag == False:
            print('#{} {}'.format(tc, cnt))
            break

