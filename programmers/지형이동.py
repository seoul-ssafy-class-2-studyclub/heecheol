from pprint import pprint


def solution(land, height):
    import collections
    import heapq

    # make island
    n = len(land)
    visit = [[False] * n for _ in range(n)]
    adj_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    mark = 0
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                mark += 1
                visit[i][j] = mark
                queue = collections.deque([(i, j)])
                while queue:
                    idx1, idx2 = queue.popleft()
                    for adj in adj_list:
                        nxt1, nxt2 = idx1 + adj[0], idx2 + adj[1]
                        if 0 <= nxt1 < n and 0 <= nxt2 < n and visit[nxt1][nxt2] is False:
                            diff = abs(land[nxt1][nxt2] - land[idx1][idx2])
                            if diff <= height:
                                visit[nxt1][nxt2] = mark
                                queue.append((nxt1, nxt2))

    # pprint(visit)

    inf = float('inf')
    diff_board = [[inf] * (mark + 1) for _ in range(mark + 1)]

    adj_list_for_ladder = [(0, 1), (1, 0)]

    for x1 in range(n):
        for y1 in range(n):
            for adj in adj_list_for_ladder:
                x2, y2 = x1 + adj[0], y1 + adj[1]
                if x2 < n and y2 < n:
                    if visit[x1][y1] != visit[x2][y2]:
                        diff = abs(land[x1][y1] - land[x2][y2])
                        if diff < diff_board[visit[x1][y1]][visit[x2][y2]]:
                            diff_board[visit[x1][y1]][visit[x2][y2]] = diff_board[visit[x2][y2]][visit[x1][y1]] = diff

    # print(queue)

    def merge(p1, q1, pre, post):
        queue_merge = collections.deque([(p1, q1)])
        visit[p1][q1] = post

        while queue_merge:
            p1, q1 = queue_merge.popleft()
            for adj in adj_list:
                p2, q2 = p1 + adj[0], q1 + adj[1]
                if 0 <= p2 < n and 0 <= q2 < n and visit[p2][q2] == pre:
                    visit[p2][q2] = post
                    queue_merge.append((p2, q2))

    answer = 0

    pprint(diff_board)
    heap = []

    for i in range(1, mark):
        for j in range(i+1, mark + 1):
            if diff_board[i][j] != inf:
                heapq.heappush(heap, [diff_board[i][j], i, j])

    while heap:
        diff, x, y = heapq.heappop(heap)
        if diff_board[x][y] != inf:
            answer += diff
    #
    # while heap:
    #     diff, x1, y1, x2, y2 = heapq.heappop(heap)
    #     if visit[x1][y1] != visit[x2][y2]:
    #         # print(x1, y1, 'value: ', visit[x1][y1], x2, y2, 'value: ', visit[x2][y2], 'diff: ', diff)
    #         answer += diff
    #         merge(x1, y1, visit[x1][y1], visit[x2][y2])
    #         mark -= 1
    #         if mark == 1:
    #             break

    # pprint(visit)
    # print(answer)

    return answer


input_land = [[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]
input_height = 1
solution(input_land, input_height)
