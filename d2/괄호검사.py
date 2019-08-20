for tc in range(int(input())):

    input_data = list(input())

    opener = {'{': '}', '(': ')'}
    closer = ['}', ')']

    stack = []

    for char in input_data:
        if char in list(opener.keys()):
            char2 = opener[char]
            stack.append(char2)
        elif char in closer:
            if len(stack) != 0:
                check = stack.pop()
                if char != check:
                    print('#{} 0'.format(tc+1))
                    break
            else:
                print('#{} 0'.format(tc+1))
                break
        else:
            pass
    else:
        if len(stack) == 0:
            print('#{} 1'.format(tc+1))
        else:
            print('#{} 0'.format(tc+1))
