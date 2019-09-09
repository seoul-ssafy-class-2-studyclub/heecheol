import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    cheeze = list(map(int, input().split()))
    pizza = []
    for idx, value in enumerate(cheeze, start=1):
        pizza.append([idx, value])
        
    queue = pizza[:N]
    pizza = pizza[N:]

    while len(queue) > 1:
        
        pull = queue.pop(0)
        pull[1] //= 2
        
        if pull[1] == 0:
            if len(pizza) != 0:
                push = pizza.pop(0)
                queue.append(push)
        else:
            queue.append(pull)

    print('#{} {}'.format(tc, queue[0][0]))
     
