import collections


def solution(tickets):
    N = len(tickets)
    answer = ['ICN']

    def fly(k, path):
        if k == N:
            return path

        departure = path[-1]
        if routes[departure]:
            for _ in range(len(routes[departure])):
                arrival = routes[departure].pop(0)
                path.append(arrival)
                if fly(k+1, path):
                    return path
                else:
                    path.pop()
                    routes[departure].append(arrival)

        return False

    routes = collections.defaultdict(list)
    for a, b in tickets:
        routes[a].append(b)

    for value in routes.values():
        value.sort()

    # print(routes)
    answer = fly(0, answer)

    return answer


print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL', 'SFO']]))
