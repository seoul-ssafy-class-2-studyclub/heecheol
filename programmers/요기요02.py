# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    new = []
    for i in range(len(S)):
        if S[i] == '-' or S[i] == ' ':
            continue
        else:
            new += S[i]

    L = len(new)

    result = ''
    if L % 3 == 1:
        if L // 3 == 1:
            result = ''.join(new[:2]) + '-' + ''.join(new[2:])
        else:
            Lleft = new[:-4]
            Lright = new[-4:]
            part = Lleft[0]
            for i in range(1, len(Lleft)):
                if i % 3 == 0:
                    result += part + '-'
                    part = Lleft[i]
                else:
                    part += Lleft[i]
            result += part + '-' + ''.join(Lright[:2]) + '-' + ''.join(Lright[2:])

    else:
        part = new[0]
        for i in range(1, L):
            if i % 3 == 0:
                result += part + '-'
                part = new[i]
            else:
                part += new[i]

        result += part

    return result
