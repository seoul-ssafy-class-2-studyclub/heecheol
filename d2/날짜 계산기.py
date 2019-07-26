# 날짜 세기

T = int(input())

for t in range(1, T + 1):

    calender = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    dict_day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    first_Month, first_Day, second_Month, second_Day = map(int, input().split())
    days = 0

    if first_Month + 1 < second_Month:
        months = calender[first_Month : second_Month - 1]   # months between two days
        
        for month in months:    # days in those months
            days += dict_day[month]
        
        # days in Second Month
        days += second_Day

        # days in First Month
        first_month_days = dict_day[first_Month] - first_Day + 1
        days += first_month_days

    elif first_Month + 1 == second_Month:   # there is no month between two days
        
        days += second_Day

        first_month_days = dict_day[first_Month] - first_Day + 1
        days += first_month_days

    else:
        days += second_Day - first_Day + 1

    print(f'#{t} {days}')

