import sys
sys.stdin = open('input.txt', 'r')


N = int(input())
input_depth = list(map(int, input().split()))

end = max(input_depth)
counts = [1] + [0] * end
flag = True
for i in range(N - 1):
    depth = input_depth[i]
    if counts[depth] + 1 > counts[depth - 1] * 2:
        flag = False
        break
    counts[input_depth[i]] += 1

if flag is False:
    print(-1)
else:
    numbers = list(range(1, N + 1))
    depth = end
    result = [[0] * counts[i] for i in range(depth + 1)]
    num = 1
    while depth >= 0:
        idx = 0
        for i in range(counts[depth]):
            result[depth][i] = numbers.pop(idx)
            idx += 1
        depth -= 1

    answer = [str(result[0][0])] + ['0'] * (N - 1)

    for i in range(N - 1):
        str_num = str(result[input_depth[i]].pop(0))
        answer[i + 1] = str_num

    print(' '.join(answer))
