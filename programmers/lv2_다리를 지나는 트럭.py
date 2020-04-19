def solution(bridge_length, limit, truck_weights):

    import collections

    answer = 0
    bridge = collections.deque([0] * bridge_length)
    truck_idx = 0
    truck_cnt = len(truck_weights)
    weight = 0

    while weight != 0 or truck_idx < truck_cnt:
        answer += 1
        weight -= bridge[-1]
        bridge[-1] = 0
        bridge.rotate(1)

        if truck_idx < truck_cnt and weight + truck_weights[truck_idx] <= limit:
            bridge[0] = truck_weights[truck_idx]
            truck_idx += 1
            weight += bridge[0]

    return answer


length = 100
w = 100
trucks = [10,10,10,10,10,10,10,10,10,10]
solution(length, w, trucks)
