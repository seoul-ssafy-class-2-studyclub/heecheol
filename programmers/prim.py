import collections
import heapq


def prim(start_node, edges):

    adj_edges = collections.defaultdict(list)

    for weight, n1, n2 in edges:
        adj_edges[n1].append((weight, n1, n2))
        adj_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    queue = adj_edges[start_node]
    heapq.heapify(queue)

    result = []
    while queue:
        weight, n1, n2 = heapq.heappop(queue)
        if n2 in connected_nodes:
            continue
        else:
            connected_nodes.add(n2)
            result.append((weight, n1, n2))

            for edge in adj_edges[n2]:
                if edge[2] not in connected_nodes:
                    heapq.heappush(queue, edge)

    return result


myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

print(prim('A', myedges))
