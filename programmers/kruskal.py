import heapq


class DisjointSet:
    def __init__(self, n):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1

        elif self.rank[root1] == self.rank[root2]:
            self.parent[root1] = root2
            self.rank[root2] += 1

        else:
            self.parent[root1] = root2


def kruskal(n, info):
    queue = []
    for i in range(len(info)):
        a, b, c = info[i]
        heapq.heappush(queue, [c, a, b])

    minimum_weight = 0
    djs = DisjointSet(n)
    result = []
    while queue:
        weight, u, v = heapq.heappop(queue)
        root_u = djs.find(u)
        root_v = djs.find(v)
        if root_u != root_v:
            djs.union(root_u, root_v)
            result.append([u, v, weight])
            minimum_weight += weight

    return result, minimum_weight


answer = kruskal(6, [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]])
print(answer)
