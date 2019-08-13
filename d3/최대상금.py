import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    init_num, chance = input().split()
    
    nums = list(init_num)
    chance = int(chance)

    sorted_nums = nums[:]
    sorted_nums.sort(reverse=True)
    
    print(''.join(sorted_nums))
