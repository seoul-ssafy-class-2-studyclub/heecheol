import collections


def solution(n, weak, dist):
    answer = 1

    queue = collections.deque([weak])

    while queue and dist:
        d = dist.pop()

        flag = False
        for _ in range(len(queue)):
            weak = queue.popleft()
            for i in range(len(weak)):
                temp = weak[:]
                if 0 <= temp[i] - d <= temp[0]:
                    temp[:i+1] = []

                elif temp[i] - d > temp[0]:
                    for j in range(i - 1, -1, -1):
                        if temp[j] < temp[i] - d:
                            temp[j+1:i+1] = []
                            break

                else:
                    for j in range(len(temp) - 1, i - 1, -1):
                        if temp[j] < n + temp[i] - d:
                            temp[j+1:] = []
                            temp[:i+1] = []
                            break

                if temp:
                    queue.append(temp)
                else:
                    flag = True
                    break

            if flag:
                return answer

        answer += 1

    return -1


print(solution(12, [10], [3, 5, 7]))