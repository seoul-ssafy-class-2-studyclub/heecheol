import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(T):
    N = int(input())

    people = [(0, 0)] * N
    result1 = [0] * N
    result2 = [0] * N

    for i in range(N):
        t1, t2 = map(int, input().split())
        people[i] = (t1 - 1, t2 - 1)
        result1[t1 - 1] = i
        result2[t2 - 1] = i

    passed = [0] * N
    p1 = result1[0]
    p2 = result2[0]
    passed[p1] = passed[p2] = 1

    e1 = people[p2][0]
    e2 = people[p1][1]

    s1 = s2 = 1

    while True:

        if s1 == e1:
            break

        man = result1[s1]
        if people[man][1] < e2:
            passed[man] = 1
            e2 = people[man][1]

        if e2 <= s2:
            break

        s1 += 1

    # print(passed)
    print(sum(passed))