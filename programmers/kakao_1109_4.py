def solution(k, room_number):
    import collections

    def make_set(v):
        parent[v] = v

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    parent = {}
    for v in range(k + 1):
        make_set(v)

    answer = collections.deque()
    visit = [False] * (k + 1)

    for num in room_number:
        if visit[num] is False:
            answer.append(num)
            visit[num] = True
            parent[num] = find(num + 1)

        else:
            nxt = find(num + 1)
            visit[nxt] = True
            answer.append(nxt)
            parent[num] = parent[nxt] = find(nxt + 1)

    return list(answer)


kk = 10
input_room = [1,3,4,1,3,1]
print(solution(kk, input_room))