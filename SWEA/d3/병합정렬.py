import sys
sys.stdin = open('input.txt', 'r')


def merge_sort(arr):
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    else:
        mid = len_arr // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)


def merge(arr_left, arr_right):
    global cnt
    if arr_left[-1] > arr_right[-1]:
        cnt += 1

    len_left = len(arr_left)
    len_right = len(arr_right)

    sorted_arr = [0] * (len_left + len_right)
    l = h = 0
    while True:
        if arr_left[l] <= arr_right[h]:
            sorted_arr[l + h] = arr_left[l]
            l += 1
            if len_left == l:
                sorted_arr[l + h:] = arr_right[h:]
                break
        else:
            sorted_arr[l + h] = arr_right[h]
            h += 1
            if len_right == h:
                sorted_arr[l + h:] = arr_left[l:]
                break
    return sorted_arr


for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(nums)
    print('#{} {} {}'.format(tc, result[N // 2], cnt))