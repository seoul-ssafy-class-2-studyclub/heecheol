def my_max(numbers):
    max_num = numbers[0]
    index = 0
    for i in range(1, len(numbers)):
        if max_num < numbers[i]:
            max_num = numbers[i]
            index = i
    return max_num, index

def my_min(numbers):
    min_num = numbers[0]
    index = 0
    for i in range(1, len(numbers)):
        if min_num > numbers[i]:
            min_num = numbers[i]
            index = i
    return min_num, index

for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))

    for d in range(dump):
        index_max = my_max(boxes)[1]
        boxes[index_max] -= 1
        index_min = my_min(boxes)[1]
        boxes[index_min] += 1
    
    print('#{} {}'.format(i, my_max(boxes)[0] - my_min(boxes)[0]))