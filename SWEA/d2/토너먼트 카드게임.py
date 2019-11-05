import sys
sys.stdin = open('input.txt', 'r')

def match(idx1, idx2):
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    
    if rsp[idx1] == 1 and rsp[idx2] == 3:
        return idx1
    elif rsp[idx1] == 3 and rsp[idx2] == 1:
        return idx2
    elif rsp[idx1] >= rsp[idx2]:
        return idx1
    else:
        return idx2
    
def winner(idx1, idx2):
    if idx1 == idx2:
        return idx1
    elif idx2 - idx1 == 1:
        return match(idx1, idx2)
    elif idx2 - idx1 >= 2:
        p = (idx1+idx2)//2
        win1 = winner(idx1, p)
        win2 = winner(p+1, idx2)
        return match(win1, win2)

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    rsp = list(map(int, input().split()))
    result = winner(0, N-1)

    print('#{} {}'.format(tc, result+1))