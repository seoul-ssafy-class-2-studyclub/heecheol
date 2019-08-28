import sys
sys.stdin = open('input01.txt', 'r')

# dl[n] == 0
def moveup(idx1):
    stack = []
    for i in range(1, 1000 - yl[idx1]):
        for n in range(N):
            if dl[n] == 3 and xl[idx1] - i == xl[n] and yl[idx1] + i == yl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 2 and xl[idx1] + i == xl[n] and yl[idx1] + i == yl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 1 and xl[idx1] == xl[n] and yl[idx1] + 2 * i >= yl[n] and visited[n] == 0:
                stack.append(n)
        if len(stack) != 0:
            break

    if len(stack) != 0:
        stack.append(i)
        return stack
    else:
        return None

# dl[n] == 1
def movedown(idx1):
    stack = []
    for i in range(1, abs(-1000 - yl[idx1])):
        for n in range(N):
            if dl[n] == 3 and xl[idx1]-i == xl[n] and yl[idx1]-i == yl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 2 and xl[idx1]+i == xl[n] and yl[idx1]-i == yl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 0 and xl[idx1] == xl[n] and yl[idx1]-2*i <= yl[n] and visited[n] == 0:
                stack.append(n)
        if len(stack) != 0:
            break

    if len(stack) != 0:
        stack.append(i)
        return stack
    else:
        return None

# dl[n] == 2
def moveleft(idx1):
    stack = []
    for i in range(1, abs(-1000 - xl[idx1])):
        for n in range(N):
            if dl[n] == 3 and yl[idx1] == yl[n] and xl[idx1] - 2 * i <= xl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 0 and xl[idx1] - i == xl[n] and yl[idx1] - i == yl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 1 and xl[idx1] - i == xl[n] and yl[idx1] + i == yl[n] and visited[n] == 0:
                stack.append(n)
        if len(stack) != 0:
            break

    if len(stack) != 0:
        stack.append(i)
        return stack
    else:
        return None


# dl[n] == 3
def moveright(idx1):
    stack = []
    for i in range(1, 1000 - xl[idx1]):
        for n in range(N):
            if dl[n] == 2 and yl[idx1] == yl[n] and xl[idx1] + 2 * i >= xl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 0 and xl[idx1] + i == xl[n] and yl[idx1] - i == yl[n] and visited[n] == 0:
                stack.append(n)
            elif dl[n] == 1 and xl[idx1] + i == xl[n] and yl[idx1] + i == yl[n] and visited[n] == 0:
                stack.append(n)
        if len(stack) != 0:
            break

    if len(stack) != 0:
        stack.append(i)
        return stack
    else:
        return None




T = int(input())
for tc in range(T):
    N = int(input())

    visited = [0] * N
    xl = [0] * N
    yl = [0] * N
    dl = [0] * N
    kl = [0] * N

    for n in range(N):
        inputs = list(map(int, input().split()))
        xl[n] = inputs[0]
        yl[n] = inputs[1]
        dl[n] = inputs[2]
        kl[n] = inputs[3]

    for n in range(N):
        data = []
        if dl[n] == 0:
            data = moveup(n)
            if data != None:
                temp = data.pop()
                for idx2 in data:
                    check = []
                    if dl[idx2] == 1:
                        check = movedown(idx2)
                    elif dl[idx2] == 2:
                        check = moveleft(idx2)
                    elif dl[idx2] == 3:
                        check = moveright(idx2)

                    if check != None and temp == check.pop():
                        visited[idx2] = 1
                        visited[temp] = 1


        elif dl[n] == 1:
            data = movedown(n)
            if data != None:
                temp = data.pop()
                for idx2 in data:
                    check = []
                    if dl[idx2] == 0:
                        check = moveup(idx2)
                    elif dl[idx2] == 2:
                        check = moveleft(idx2)
                    elif dl[idx2] == 3:
                        check = moveright(idx2)

                    if check != None and temp == check.pop():
                        visited[idx2] = 1
                        visited[temp] = 1

        elif dl[n] == 2:
            data = moveleft(n)
            if data != None:
                temp = data.pop()
                for idx2 in data:
                    check = []
                    if dl[idx2] == 0:
                        check = moveup(idx2)
                    elif dl[idx2] == 1:
                        check = movedown(idx2)
                    elif dl[idx2] == 3:
                        check = moveright(idx2)

                    if check != None and temp == check.pop():
                        visited[idx2] = 1
                        visited[temp] = 1

        elif dl[n] == 3:
            data = moveright(n)
            if data != None:
                temp = data.pop()
                for idx2 in data:
                    check = []
                    if dl[idx2] == 0:
                        check = moveup(idx2)
                    elif dl[idx2] == 1:
                        check = movedown(idx2)
                    elif dl[idx2] == 2:
                        check = moveleft(idx2)

                    if check != None and temp == check.pop():
                        visited[idx2] = 1
                        visited[temp] = 1


    result = 0
    for n in range(N):
        if visited[n] != 0:
            print(n)
            result += kl[n]

    print(result)
