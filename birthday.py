import datetime
def birthday():
    time_now=datetime.datetime.now()
    today_year = time_now.year
    today_month =time_now.month
    today_day = time_now.day
    birthday_year = int(input("birthday_year: "))
    birthday_month = int(input("birthday_month: "))
    birthday_day = int(input("birthday day: "))
    birthday_left = int()
    def_find_year(birthday_year,birthday_month,birthday_day)
    years_old = today_year-birthday_year

    if today_month<birthday_month:
        month_left=(birthday_month-today_month)*30
        birthday_left=month_left+(birthday_day-today_day)
        print(convert_month(birthday_left))
        return f"your birthday is in {birthday_left} days."
    if today_month>birthday_month:
        month_left=(birthday_month+(12-today_month))*30
        birthday_left=month_left+(birthday_day-today_day)
        print(convert_month(birthday_left))
        return f"your birthday is in {birthday_left} days."
    if today_month==birthday_month:
        if birthday_day<today_day:
            birthday_left=(365+birthday_day)
            print(convert_month(birthday_left))
            return f"your birthday is in {birthday_left} days."
        if birthday_day>today_day:
            birthday_left=birthday_day-today_day
            return f"your birthday is in {birthday_left} days."
        return "happy birthay"

def convert_month(days):
    if days>=30:
        print(days)
        days_left = days%30

        month = (days-days_left)/30
        return month,days_left
    return days

def def_find_year(year,month,day):
    time_now=datetime.datetime.now()
    today_year = time_now.year
    today_month =time_now.month
    today_day = time_now.day
    year = year -today_year
    if today_month<month:
        month_left=(month-today_month)*30
        birthday_left=month_left+(day-today_day)
        month_day = convert_month(birthday_left)
        print("year",year)
        print("-------",month_day[0])



print(birthday())