day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day,month,year):
    days = 0
    for i in range(month - 1):
        days += day_in_month[i]

    if (is_leap(year) == True and month >= 3):
        return days + day + 1
    else:
        return days + day

def day_in_year(year):
    if is_leap(year):
        return 366
    else:
        return 355

def date_diff(x,y):
    before = [int(i) for i in x.split('-')]
    after  = [int(i) for i in y.split('-')]
    diff = day_of_year(after[0],after[1],after[2]) - day_of_year(before[0],before[1],before[2]) + ((after[2] - before[2]) * 365) + 1
    for i in range(before[2],after[2]):
        if is_leap(i):
            diff += 1
    return diff