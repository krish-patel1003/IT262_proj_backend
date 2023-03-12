from notifications.models import Notice


def parse_date(date):
    date = date.split("-")
    date_year = int(date[0])
    date_mon = int(date[1])
    date_day = int(date[2])

    return date_year, date_mon, date_day

def get_leaves():
    leaves = Notice.objects.filter(tag="Leave")
    leave_dates = []
    for leave in leaves:
        leave_dates.append([leave.on_leave_from, leave.on_leave_till])
    
    return leave_dates