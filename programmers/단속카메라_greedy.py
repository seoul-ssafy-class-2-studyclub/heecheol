def solution(routes):
    routes.sort(key=lambda x: x[1])
    N = len(routes)

    visit = [False] * N

    answer = 0
    i = 0
    while i < N:
        if visit[i]:
            i += 1

        else:
            visit[i] = True
            answer += 1

            end = routes[i][1]
            for j in range(i+1, N):
                if visit[j]:
                    continue
                elif routes[j][0] <= end:
                    visit[j] = True
            i += 1

    return answer

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])
