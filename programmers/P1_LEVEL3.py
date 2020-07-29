def solution(dirs):
    board = [[[False, False, False, False] for _ in range(11)] for __ in range(11)]

    adj = {
        'U': (-1, 0),
        'D': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }

    dir_idx = {
        'U': 0,
        'D': 2,
        'R': 1,
        'L': 3
    }

    answer = 0
    idx1 = idx2 = 5
    for d in dirs:
        nxt1, nxt2 = idx1 + adj[d][0], idx2 + adj[d][1]
        if 0 <= nxt1 < 11 and 0 <= nxt2 < 11:
            k = dir_idx[d]
            if not board[idx1][idx2][k]:
                board[idx1][idx2][k] = True
                board[nxt1][nxt2][(k+2) % 4] = True
                answer += 1
            idx1, idx2 = nxt1, nxt2

    return answer


print(solution('LULLLLLLU'))
