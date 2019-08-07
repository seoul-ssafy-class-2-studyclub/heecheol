import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input())+1):
    people = list(map(int, input()))

    hand = []

    if people[0] == 0:
        buy = 1
        hand.append(1)
    else:
        hand.append(people[0])
        buy = 0

    for i in range(1, len(people)):
    
        if sum(hand) >= i:
            hand.append(people[i])

        else:
            buy += i - sum(hand)
            hand.append(i-sum(hand))
            hand.append(people[i])

    print(f'#{tc} {buy}')

