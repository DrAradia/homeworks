from datetime import datetime

def get_days_from_today(date):
    current_date = datetime.now()
    while True:
        try:
            users_date = datetime.strptime(date, '%Y-%m-%d')
            return f'Кількість днів між введеною датою і поточною: {(users_date-current_date).days}'
        except Exception:
            date=input(f'{date} не відповідає формату дати РРРР-ММ-ДД, введіть іншу дату: ') 

print (get_days_from_today(input('Введіть дату у форматі РРРР-ММ-ДД: ')))


