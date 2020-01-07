def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] == completion[i]:
            continue
        answer = participant[i]
        break

    return answer


pp = ['mislav', 'stanko', 'mislav', 'ana']
cc = ['stanko', 'ana', 'mislav']
solution(pp, cc)