
def parse_date(date):
    date = date.split("-")
    date_year = int(date[0])
    date_mon = int(date[1])
    date_day = int(date[2])

    return date_year, date_mon, date_day
    