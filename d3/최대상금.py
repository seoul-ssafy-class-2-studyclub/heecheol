import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    init_num, chance = input().split()
    
    numbers = list(map(int, list(init_num)))
    chance = int(chance)

    print(numbers, chance)

    for i in range(len(numbers)):
        if chance == 0:
            break
        else:
            r_numbers = list(reversed(numbers))
            k = r_numbers.index(max(numbers[i:]))
            j = len(numbers) - k - 1
            if i != j:
                numbers[i], numbers[j] = numbers[j], numbers[i]
            chance -= 1
            print(i, j)
    else:
        if chance % 2:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
    
    numbers = list(map(str, numbers))
    print(''.join(numbers))
