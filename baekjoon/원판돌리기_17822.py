import collections
# from pprint import pprint
# import sys
# sys.stdin = open('input.txt', 'r')


def del_adjacency():
    visit = [[False] * M for _ in range(N)]
    indexes = set()

    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                continue
            elif board[i][j] == 0:
                continue
            else:
                visit[i][j] = True
                queue = [(i, j)]
                while queue:
                    idx1, idx2 = queue.pop(0)
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < N:
                            nxt2 = (nxt2+M) % M
                            if visit[nxt1][nxt2] is False and board[idx1][idx2] == board[nxt1][nxt2]:
                                visit[nxt1][nxt2] = True
                                queue.append((nxt1, nxt2))
                                indexes.add((idx1, idx2))
                                indexes.add((nxt1, nxt2))

    if indexes:
        for i, j in indexes:
            board[i][j] = 0
        return True

    else:
        total = 0
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    total += board[i][j]
                    cnt += 1
        if cnt:
            avg = total / cnt   # cnt 체크 필수!!!!!!!!!!!!!!!!!
            for i in range(N):
                for j in range(M):
                    if 0 < board[i][j] < avg:
                        board[i][j] += 1
                    elif board[i][j] > avg:
                        board[i][j] -= 1
            return True
        else:
            return False


N, M, T = map(int, input().split())
board = [collections.deque(list(map(int, input().split()))) for _ in range(N)]

adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(T):
    x, d, k = map(int, input().split())

    if d == 0:
        for n in range(1, N//x + 1):
            board[x*n - 1].rotate(k)
    else:
        for n in range(1, N//x + 1):
            board[x*n - 1].rotate(-k)

    if del_adjacency():
        continue
    else:
        break

print(sum([sum(row) for row in board]))
