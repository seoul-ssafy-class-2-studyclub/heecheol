import sys
sys.stdin = open('input.txt', 'r')


# T = int(input())
# for tc
N = int(input())
best_friends = [0] + list(map(int, input().split()))

order_lists = [[] for _ in range(N + 1)]
status = [0] * (N + 1)  # 0 => before check / full, part, pair, impossible

for i in range(1, N + 1):
    if status[i] == 0:
        i_list = [i]
        num = best_friends[i]
        while True:
            if status[num] == 0:
                if num not in i_list:
                    i_list.append(num)
                    num = best_friends[num]
                    continue
                if num == i_list[0]:
                    for k in range(len(i_list)):
                        idx = i_list[k]
                        order_lists[idx] = i_list[k:] + i_list[:k]
                        status[idx] = 2
                    break
                if num == i_list[-2]:
                    for k in range(len(i_list) - 1):
                        idx = i_list[k]
                        order_lists[idx] = i_list[k:]
                        status[idx] = 1
                    idx = i_list[-1]
                    order_lists[idx] = list(reversed(i_list))
                    status[idx] = 1
                    break
                for j in range(i_list.index(num)):
                    idx = i_list[j]
                    status[idx] = -1

            elif status[num] == -1:
                pass



print(status)