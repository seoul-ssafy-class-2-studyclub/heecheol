import datetime


def solution(lines):
    n = len(lines)
    time_e = [0] * n
    time_s = [0] * n

    for i in range(n):
        line = lines[i].split()
        date_time_str = ' '.join(line[:2])
        ms = int(float(line[2][:-1]) * 1000 - 1)
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
        time_e[i] = datetime.datetime.strftime(date_time_obj, '%Y-%m-%d %H:%M:%S.%f')
        time_s[i] = datetime.datetime.strftime(date_time_obj - datetime.timedelta(milliseconds=ms), '%Y-%m-%d %H:%M:%S.%f')

    answer = 1
    for i in range(n - 1):
        temp = datetime.datetime.strptime(time_e[i], '%Y-%m-%d %H:%M:%S.%f') + datetime.timedelta(milliseconds=999)
        cnt = 1
        for j in range(i + 1, n):
            if temp >= datetime.datetime.strptime(time_s[j], '%Y-%m-%d %H:%M:%S.%f'):
                cnt += 1
        if cnt > answer:
            answer = cnt

    # print(time_s)
    # print(time_e)
    # print(answer)

    return answer


data = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
solution(data)
