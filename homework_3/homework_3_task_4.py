import datetime as dt
from datetime import datetime

users = [{"name": "John Doe", "birthday": "1985.02.02"}, {"name": "Jane Smith", "birthday": "1990.02.03"}]

def get_upcoming_birthdays(users=None):
    today = datetime.today().date()
    birthdays=[]
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(year=today.year, month=birthday_date.month, day=birthday_date.day).date()
        if birthday_this_year < today:
            birthday_this_year = datetime(year=today.year+1, month=birthday_date.month, day=birthday_date.day).date()
        else:
            pass
        week_day=birthday_this_year.isoweekday()
        days_between=(birthday_this_year-today).days
        if 0<=days_between<=7: 
            if week_day<=5: 
                birthdays.append({'name':user['name'], 'birthday':birthday_this_year.strftime("%Y.%m.%d")}) 
            else:
                if (birthday_this_year+dt.timedelta(days=1)).weekday()==0:
                    birthdays.append({'name':user['name'], 'birthday':(birthday_this_year+dt.timedelta(days=1)).strftime("%Y.%m.%d")})
                elif (birthday_this_year+dt.timedelta(days=2)).weekday()==0: 
                    birthdays.append({'name':user['name'], 'birthday':(birthday_this_year+dt.timedelta(days=2)).strftime("%Y.%m.%d")})
    return birthdays

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))

