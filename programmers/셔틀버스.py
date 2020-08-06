import datetime


def solution(n, t, m, timetable):
    nine = datetime.datetime.strptime('09:00:01', '%H:%M:%S')
    departures = [nine]

    for _ in range(n-1):
        nxt = departures[-1] + datetime.timedelta(minutes=t)
        departures.append(nxt)

    for i in range(len(timetable)-1, -1, -1):
        if timetable[i] > '18:01':
            timetable.pop(i)
        else:
            timetable[i] = datetime.datetime.strptime(timetable[i], '%H:%M')

    timetable.sort()
    length = len(timetable)

    # people = [[] for _ in range(n)]
    # for i in range(n):
    #     for _ in range(m):
    #         if len(timetable) and timetable[0] < departures[i]:
    #             people[i].append(timetable.pop(0))
    #         else:
    #             break

    idx = 0
    for i in range(n):
        cnt = 0
        for _ in range(m):
            if idx < length and timetable[idx] < departures[i]:
                idx += 1
                cnt += 1
            else:
                break

    if cnt < m:
        answer = departures[-1]
        return datetime.datetime.strftime(answer, '%H:%M')
    else:
        answer = timetable[idx-1] - datetime.timedelta(minutes=1)
        return datetime.datetime.strftime(answer, '%H:%M')
