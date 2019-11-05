import sys
sys.stdin = open('input.txt', 'r')


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    elif rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root1] = root2
        rank[root2] += 1


def kruskal():
    for v in range(V + 1):
        make_set(v)

    for edge in temp_list:
        weight, v1, v2 = edge

        if find(v1) != find(v2):
            union(v1, v2)
            mst.append(weight)
            if len(mst) == V:
                return


for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    parent = {}
    rank = {}
    temp_list = [0] * E
    mst = []

    for i in range(E):
        n1, n2, w = map(int, input().split())
        temp_list[i] = (w, n1, n2)

    temp_list.sort()
    kruskal()

    print('#{} {}'.format(tc, sum(mst)))
