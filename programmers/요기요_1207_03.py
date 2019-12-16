# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    cnt = 1
    part = ''
    for i in range(len(S)):
        if S[i] in part:
            part = S[i]
            cnt += 1
        else:
            part += S[i]

    return cnt


string = 'abacdec'
solution(string)
