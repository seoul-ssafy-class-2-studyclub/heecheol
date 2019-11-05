TC = int(input())
for tc in range(1, TC+1):
    data = list(input().split())

    operator = ['+', '-', '*', '/']
    flag = True

    while flag == True:
        length = len(data)

        if length == 2:
            result = data[0]
            break

        for i in range(length):
            if data[i] in operator:
                if i < 2:
                    flag = False
                    result = 'error'
                    break
                else:
                    num1 = data.pop(i-2)
                    num2 = data.pop(i-2)
                    op = data.pop(i-2)
                    if op == '+':
                        num3 = int(num1) + int(num2)
                    elif op == '-':
                        num3 = int(num1) - int(num2)
                    elif op == '*':
                        num3 = int(num1) * int(num2)
                    else:
                        num3 = int(num1) // int(num2)
                    data.insert(i-2, num3)
                    break
        else:
            flag = False
            result = 'error'
            break

    print('#{} {}'.format(tc, result))

