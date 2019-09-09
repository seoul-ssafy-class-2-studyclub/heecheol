import sys
sys.stdin = open('input.txt', 'r')

R, C, M = map(int, input().split())

rl = [0]*(M+1)  # row
cl = [0]*(M+1)  # col
sl = [0]*(M+1)  # speed
dl = [0]*(M+1)  # direction
zl = [0]*(M+1)  # size

for m in range(1, M+1):
    rl[m], cl[m], sl[m], dl[m], zl[m] = map(int, input().split())

person_col = 1

while True:




    if person_col == C:
        break
    person_col += 1
