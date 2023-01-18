def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day,month,year):
    m = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(month - 1):
        days += m[i]
    if (is_leap(year) == True and month >= 3):
        return days + day + 1
    else:
        return days + day