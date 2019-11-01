import sys
sys.stdin = open('input.txt', 'r')


def move(idx, score):
    global max_score

    if idx == 10:
        if score > max_score:
            max_score = score
        return

    else:
        num = dices[idx]

        for i in range(32):
            if positions[i]:
                nxt = moving[i][num - 1]
                if positions[nxt]:
                    continue
                else:
                    positions[i].pop()
                    if nxt == 32:
                        move(idx + 1, score)
                    else:
                        positions[nxt].append(1)
                        move(idx + 1, score + scores[nxt])
                        positions[nxt].pop()
                    positions[i].append(1)


positions = [[] for _ in range(33)]
positions[0] = [1, 1, 1, 1]

moving = {
    0: [1, 2, 3, 4, 5],
    1: [2, 3, 4, 5, 6],
    2: [3, 4, 5, 6, 7],
    3: [4, 5, 6, 7, 8],
    4: [5, 6, 7, 8, 9],
    5: [21, 22, 23, 29, 30],
    6: [7, 8, 9, 10, 11],
    7: [8, 9, 10, 11, 12],
    8: [9, 10, 11, 12, 13],
    9: [10, 11, 12, 13, 14],
    10: [24, 25, 29, 30, 31],
    11: [12, 13, 14, 15, 16],
    12: [13, 14, 15, 16, 17],
    13: [14, 15, 16, 17, 18],
    14: [15, 16, 17, 18, 19],
    15: [26, 27, 28, 29, 30],
    16: [17, 18, 19, 20, 32],
    17: [18, 19, 20, 32, 32],
    18: [19, 20, 32, 32, 32],
    19: [20, 32, 32, 32, 32],
    20: [32, 32, 32, 32, 32],
    21: [22, 23, 29, 30, 31],
    22: [23, 29, 30, 31, 20],
    23: [29, 30, 31, 20, 32],
    24: [25, 29, 30, 31, 20],
    25: [29, 30, 31, 20, 32],
    26: [27, 28, 29, 30, 31],
    27: [28, 29, 30, 31, 20],
    28: [29, 30, 31, 20, 32],
    29: [30, 31, 20, 32, 32],
    30: [31, 20, 32, 32, 32],
    31: [20, 32, 32, 32, 32],
}

scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 22, 24, 28, 27, 26, 25, 30, 35, 0]

dices = list(map(int, input().split()))
max_score = 0
move(0, 0)
print(max_score)
