# https://programmers.co.kr/learn/courses/30/lessons/42626


def solution(scoville, k):
    import heapq

    heapq.heapify(scoville)
    # scovile의 길이가 최대 1,000,000 이라
    # for문으로 k보다 작은것들만 heap에 넣어줬는데
    # 오히려 시간이 더 걸렸다.

    answer = 0

    flag = False
    while True:
        if len(scoville) > 1:
            s1 = heapq.heappop(scoville)
            if s1 >= k:
                return answer

            s2 = heapq.heappop(scoville)
            answer += 1

            mixed = s1 + (s2 * 2)
            if mixed < k:
                heapq.heappush(scoville, mixed)
                continue

            if not flag:
                flag = True
                continue

        elif not flag:
            return -1

        elif len(scoville):
            return answer + 1

        else:
            return answer


print(solution([5, 3, 2], 11))
