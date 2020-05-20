# https://programmers.co.kr/learn/courses/30/lessons/42586


def solution(progresses, speeds):
    import math

    n = len(progresses)
    answer = []
    idx = 0
    while idx < n:
        if progresses[idx] >= 100:
            idx += 1
        else:
            day = math.ceil((100 - progresses[idx]) / speeds[idx])
            progresses[idx] = 100
            cnt = 1
            flag = True
            for j in range(idx + 1, n):
                progresses[j] += speeds[j] * day
                if flag:
                    if progresses[j] >= 100:
                        cnt += 1
                    else:
                        flag = False

            answer.append(cnt)
            idx += 1

    return answer


solution([93, 30, 55, 60], [1, 30, 5, 40])
