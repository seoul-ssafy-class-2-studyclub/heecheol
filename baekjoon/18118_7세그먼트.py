import heapq
import sys
sys.stdin = open('input.txt', 'r')


def push_to_heap(k, string):
    if k == n:
        num = int(''.join(list(string)))
        heapq.heappush(str_nums, (-num, num))
        return
    else:
        for c in c_nums:
            push_to_heap(k + 1, string + c)


t = int(input())
c_nums = ['11', '9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
for tc in range(t):
    max_num = 0
    n, m = map(int, input().split())

    str_nums = []
    push_to_heap(0, '')

    while True:
        number = heapq.heappop(str_nums)[1]
        if number % m == 0:
            break
    print(number)

