import sys
sys.stdin = open('input.txt', 'r')


def solution(s):
    length = len(s)
    answer = 987654321

    if length <= 2:
        answer = length

    else:
        for i in range(1, length // 2 + 1):
            string = s
            begin = 0
            end = i
            spl = []

            while string:
                spl.append(string[begin:end])
                string = string[end:]

            cnt = 1
            new_string = ''

            for i in range(len(spl) - 1):
                if spl[i] == spl[i + 1]:
                    cnt += 1
                else:
                    if cnt == 1:
                        new_string += spl[i]
                    else:
                        new_string += str(cnt) + spl[i]
                    cnt = 1
            if cnt == 1:
                new_string += spl[-1]
            else:
                new_string += str(cnt) + spl[-1]

            if answer > len(new_string):
                answer = len(new_string)

    return answer


string = input()
print(solution(string))
