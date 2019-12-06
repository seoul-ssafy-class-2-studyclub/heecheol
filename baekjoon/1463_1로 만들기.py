import sys
sys.stdin = open('input.txt', 'r')


def function(num, cnt):
    global result

    if cnt >= result:
        return

    if num == 1:
        result = cnt
        return

    else:
        if num % 3 == 0:
            function(num // 3, cnt + 1)
        if num % 2 == 0:
            function(num // 2, cnt + 1)

        function(num - 1, cnt + 1)


result = 987654321
N = int(input())

function(N, 0)

print(result)
