import sys
sys.setrecursionlimit(100000)


def solution(nodeinfo):
    answer = [[], []]

    n = len(nodeinfo)
    for i in range(n):
        nodeinfo[i].append(i+1)

    parent = [0] * (n+1)
    child_left = [0] * (n+1)
    child_right = [0] * (n+1)

    def tree(arr, n_parent):
        if len(arr) == 0:
            return False

        arr.sort()
        m = 0
        for k in range(1, len(arr)):
            if arr[k][1] > arr[m][1]:
                m = k

        parent[arr[m][2]] = n_parent
        left_side = arr[:m]
        right_side = arr[m+1:]

        left = tree(left_side, arr[m][2])
        if left:
            child_left[arr[m][2]] = left

        right = tree(right_side, arr[m][2])
        if right:
            child_right[arr[m][2]] = right

        return arr[m][2]

    def preorder(node):
        answer[0].append(node)

        if child_left[node] != 0:
            preorder(child_left[node])
        if child_right[node] != 0:
            preorder(child_right[node])

    def postorder(node):

        if child_left[node] != 0:
            postorder(child_left[node])

        if child_right[node] != 0:
            postorder(child_right[node])

        answer[1].append(node)

    top_node = tree(nodeinfo, 0)

    preorder(top_node)
    postorder(top_node)

    return answer


print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[22,22]]))
