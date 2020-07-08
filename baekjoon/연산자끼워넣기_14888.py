import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

queue = [[operators, numbers[0]]]

for n in range(1, N):
    num_back = numbers[n]
    for _ in range(len(queue)):
        ops, num_front = queue.pop(0)
        for i in range(4):
            if ops[i] > 0:
                temp = ops[:]
                temp[i] -= 1
                if i == 0:
                    queue.append([temp, num_front + num_back])
                elif i == 1:
                    queue.append([temp, num_front - num_back])
                elif i == 2:
                    queue.append([temp, num_front * num_back])
                elif num_front >= 0:
                    queue.append([temp, num_front // num_back])
                else:
                    queue.append([temp, -(abs(num_front) // num_back)])

queue_sort = sorted(queue, key=lambda x: x[1])
print(queue_sort[-1][1])
print(queue_sort[0][1])
