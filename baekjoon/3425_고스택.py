import sys
sys.stdin = open('input.txt', 'r')


flag = True
while True:
    O = []
    while True:
        opr = input()
        if opr == 'END':
            break
        if opr == 'QUIT':
            flag = False
            break
        if len(opr) > 3:
            O.append(opr.split()[1])
            continue
        O.append(opr[:2])

    if flag is False:
        break

    # print(O)

    N = int(input())
    input_nums = [0] * N
    for i in range(N):
        input_nums[i] = int(input())

    empty = input()

    for num in input_nums:
        nums = [num]
        idx = 0

        flag1 = True
        for opr in O:
            if opr.isdigit():
                if idx + 1 == len(nums):
                    nums.append(int(opr))
                    idx += 1
                else:
                    nums[idx + 1] = int(opr)
                    idx += 1

            else:
                if opr == 'PO':
                    if idx == -1:
                        flag1 = False
                        break
                    idx -= 1

                elif opr == 'IN':
                    if idx == -1:
                        flag1 = False
                        break
                    nums[idx] *= -1

                elif opr == 'DU':
                    if idx == -1:
                        flag1 = False
                        break
                    if idx + 1 == len(nums):
                        nums.append(nums[idx])
                        idx += 1
                    else:
                        nums[idx + 1] = nums[idx]
                        idx += 1

                elif opr == 'SW':
                    if idx <= 0:
                        flag1 = False
                        break
                    nums[idx - 1], nums[idx] = nums[idx], nums[idx - 1]

                elif opr == 'AD':
                    if idx <= 0:
                        flag1 = False
                        break
                    nums[idx - 1] += nums[idx]
                    idx -= 1

                elif opr == 'SU':
                    if idx <= 0:
                        flag1 = False
                        break
                    nums[idx - 1] -= nums[idx]
                    idx -= 1

                elif opr == 'MU':
                    if idx <= 0:
                        flag1 = False
                        break
                    nums[idx - 1] *= nums[idx]
                    idx -= 1

                elif opr == 'DI':
                    if idx <= 0 or nums[idx] == 0:
                        flag1 = False
                        break
                    if nums[idx - 1] * nums[idx] >= 0:
                        nums[idx - 1] //= nums[idx]
                        idx -= 1
                    else:
                        nums[idx - 1] = -(abs(nums[idx - 1]) // abs(nums[idx]))
                        idx -= 1

                elif opr == 'MO':
                    if idx <= 0 or nums[idx] == 0:
                        flag1 = False
                        break
                    if nums[idx - 1] > 0:
                        nums[idx - 1] %= abs(nums[idx])
                        idx -= 1
                    else:
                        nums[idx - 1] = -(abs(nums[idx - 1]) % abs(nums[idx]))
                        idx -= 1

                if abs(nums[idx]) > 1e9:
                    flag1 = False
                    break

        if flag1 is False or idx != 0:
            print('ERROR')
        else:
            print(nums[0])

    print()