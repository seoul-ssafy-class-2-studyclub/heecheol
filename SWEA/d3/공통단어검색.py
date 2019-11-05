import sys
sys.stdin = open('input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    A_word = []
    for i in range(N):
        A_word.append(input())

    cnt = 0
    for i in range(M):
        B_word = input()
        if B_word in A_word:
            cnt += 1
            
    print(cnt)


