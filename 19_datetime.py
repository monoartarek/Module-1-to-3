from datetime import date, timedelta

current_date = date.today()
next_date = current_date + timedelta(days = 10)

print(current_date)
print(next_date)