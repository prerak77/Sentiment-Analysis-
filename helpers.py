import calendar
from datetime import datetime, timedelta


# function to return the next date of teh current date
def get_next_date(current_date):
    # Convert the input date string to a datetime object
    current_date = datetime.strptime(current_date, '%Y-%m-%d')

    # Calculate the next date by adding one day
    next_date = current_date + timedelta(days=1)

    # Convert the next date back to a string
    next_date_str = next_date.strftime('%Y-%m-%d')

    return next_date_str


# function to return all teh dates in a given month and year
def get_dates_in_month(year, month):
    cal = calendar.monthcalendar(year, month)
    dates_in_month = [day for week in cal for day in week if day != 0]
    return dates_in_month
