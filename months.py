import calendar
def months():
    for i in calendar.month_name:
        if i:
            print(i)
months()