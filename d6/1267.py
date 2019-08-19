import sys
sys.stdin = open('input.txt', 'r')
import copy

for tc in range(5):

    V, E = map(int, input().split())

    order = []
    inputs = list(input().split())


    for i in range(E):
        temp = []
        temp.append(inputs.pop(0))
        temp.append(inputs.pop(0))
        order.append(temp)

    result = [order[0][0], order[0][1]]
    last_order = []

    for i in range(1, E):
        # print(order[i][0], order[i][1])
        if order[i][0] in result and order[i][1] in result:
            pass

        elif order[i][0] in result and order[i][1] not in result:
            k = result.index(order[i][0])
            result.insert(k+1, order[i][1])
            result[k+1] = order[i][1]

        elif order[i][0] not in result and order[i][1] in result:
            k = result.index(order[i][1])
            result.insert(k, order[i][0])

        else:
            last_order.append([order[i][0], order[i][1]])
    print('===============================================')
    print(result)
    print(last_order)
    
    while len(last_order) > 0:
        temp2 = len(last_order)
        order = copy.deepcopy(last_order)
        last_order = []
        for i in range(len(order)):
            if order[i][0] in result and order[i][1] in result:
                pass

            elif order[i][0] in result and order[i][1] not in result:
                k = result.index(order[i][0])
                result.insert(k+1, order[i][1])
                result[k+1] = order[i][1]

            elif order[i][0] not in result and order[i][1] in result:
                k = result.index(order[i][1])
                result.insert(k, order[i][0])
                
            else:
                last_order.append([order[i][0], order[i][1]])

        temp = len(last_order)                
        if temp == temp2 and temp != 0:
            result.append(last_order[0][0])
            result.append(last_order[0][1])
    
    # reresult = ' '.join(result)
    # print(f'#{tc} {reresult}')