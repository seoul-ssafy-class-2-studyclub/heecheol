from pprint import pprint
import sys
sys.stdin = open('input.txt', 'r')


def check():
    cnt = 0
    visit = [[False] * (w + 2) for _ in range(h + 2)]
    queue = [(0, 0)]
    while queue:
        idx1, idx2 = queue.pop(0)
        for adj in adj_list:
            nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
            if 0 <= nxt1 < h + 2 and 0 <= nxt2 < w + 2:
                data = board[nxt1][nxt2]
                if data == '*' or visit[nxt1][nxt2] is True:
                    continue
                if data == '.':
                    queue.append((nxt1, nxt2))
                    visit[nxt1][nxt2] = True
                    continue
                if data == '$':
                    queue.append((nxt1, nxt2))
                    visit[nxt1][nxt2] = True
                    cnt += 1
                    continue
                ascii_data = ord(data)
                if 65 <= ascii_data <= 90:
                    index = ascii_data - 65
                    if keys[index] == 1:
                        queue.append((nxt1, nxt2))
                        visit[nxt1][nxt2] = True
                        continue
                    else:
                        doors[index] += 1
                        p_doors[index].append((nxt1, nxt2))
                        continue
                elif 97 <= ascii_data <= 122:
                    index = ascii_data - 97
                    keys[index] = 1
                    queue.append((nxt1, nxt2))
                    visit[nxt1][nxt2] = True
                    if doors[index] == 0:
                        continue
                    else:
                        for _ in range(doors[index]):
                            d1, d2 = p_doors[index].pop()
                            queue.append((d1, d2))
                            visit[d1][d2] = True
                        doors[index] = 0
                        continue
    return cnt


T = int(input())
adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for _ in range(T):
    h, w = map(int, input().split())
    board = [['.'] * (w + 2) for _ in range(2)]
    for i in range(h):
        board.insert(i + 1, ['.'] + list(input()) + ['.'])

    K = list(input())
    keys = [0] * 26
    doors = [0] * 26
    p_doors = [[] for _ in range(26)]

    if K[0] == '0':
        result = check()
        print(result)
    else:
        for i in range(len(K)):
            k = ord(K[i]) - ord('a')
            keys[k] = 1
        result = check()
        print(result)
