import time
from datetime import date, timedelta

def first_day_of_month(time_tuple):
    return date(time_tuple.tm_year, time_tuple.tm_mon, 1)

def last_day_of_month(time_tuple):
    twenty_night_days = first_day_of_month(time_tuple) + timedelta(days = 28)
    one_day_delta = timedelta(days = 1)
    for d in range(3):
        if (twenty_night_days + one_day_delta * d).month > twenty_night_days.month:
            return 28 + d
    return 31

def print_title(time_tuple):
    print('     {}'.format(time.strftime('%B %Y', first_day_of_month(time_tuple).timetuple())))
    wday_names = ['MO', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
    for wday_name in wday_names:
        print('{} '.format(wday_name), end = '')
    print()

def print_days(time_tuple):
    wday_count = time_tuple.tm_wday + 1
    for i in range(wday_count - 1):
        print('   ', end = '')

    last = last_day_of_month(time_tuple)
    for day in range(1, last + 1):
        print('{0:2d} '.format(day), end = ('\n' if wday_count % 7 == 0 else ''))
        wday_count += 1

today = time.gmtime()
print_title(today)
print_days(today)

