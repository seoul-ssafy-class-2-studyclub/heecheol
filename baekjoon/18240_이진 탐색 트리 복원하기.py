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
    numbers = list(range(N + 1))
    next_number = list(range(1, N + 2))

    depth = end
    result = [[0] * counts[i] for i in range(depth + 1)]

    start = 1
    while depth >= 0:
        idx = start
        start = next_number[idx]

        for i in range(counts[depth] - 1):
            result[depth][i] = idx
            nxt = next_number[idx]
            n_nxt = next_number[nxt]
            next_number[nxt] = next_number[n_nxt]
            idx = n_nxt

        result[depth][-1] = idx
        depth -= 1

    answer = [str(result[0][0])] + ['-'] * (N - 1)

    for i in range(N - 1):
        answer[i + 1] = str(result[input_depth[i]].pop(0))

    print(' '.join(answer))
