import collections


def solution(priorities, location):
    answer = 0
    queue = collections.deque(list(range(len(priorities))))

    top = max(priorities)
    while True:
        if priorities[queue[0]] == top:
            i = queue.popleft()
            answer += 1
            if i == location:
                return answer
            priorities[i] = 0
            top = max(priorities)
        else:
            queue.rotate(-1)


print(solution([2, 1, 3, 2], 2))
