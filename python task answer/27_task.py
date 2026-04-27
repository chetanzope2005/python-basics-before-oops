import datetime as dt

current_date = dt.date.today()

next_year = current_date.year + 1
new_year = dt.date(next_year, 1, 1)

print (f"Current date: {current_date}")
print (f"New Year: {new_year}")
months_until_new_year = 12 - current_date.month
days_until_new_year = (new_year - current_date).days
print(f"Days until New Year: {days_until_new_year} or in months: {months_until_new_year}")
