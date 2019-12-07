def solution(A, B, C, D):
    import itertools

    given = [A, B, C, D]
    perms = list(set(itertools.permutations(given)))
    cnt = 0
    for perm in perms:
        if perm[0] > 2 or perm[2] > 5:
            continue
        elif perm[0] == 2 and perm[1] > 3:
            continue
        else:
            cnt += 1

    return cnt


solution(1, 8, 3, 2)
