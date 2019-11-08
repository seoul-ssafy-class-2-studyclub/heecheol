import sys
sys.stdin = open('input.txt', 'r')


def solution(p):
    if len(p) == 0:
        return p

    def modify(w):
        if len(w) == 0:
            return w
        else:
            flag = 0
            for i in range(len(w)):
                if w[i] == '(':
                    flag += 1
                else:
                    flag -= 1
                if flag == 0:
                    break
            u = w[:i + 1]
            v = w[i + 1:]
            if u[0] == '(':
                if len(v) == 0:
                    return u
                else:
                    return u + modify(v)

            else:
                s = list(u)

                for j in range(1, len(s) - 1):
                    if s[j] == '(':
                        s[j] = ')'
                    else:
                        s[j] = '('

                u = ''.join(s[1:-1])

                if len(v) == 0:
                    return '(' + ')' + u
                else:
                    return '(' + modify(v) + ')' + u

    answer = modify(p)
    return answer


p = input()
print(solution(p))
