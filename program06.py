#  program to print date , time for today and now seperately.
import datetime

current_date = datetime.date.today()
current_time = datetime.datetime.now().time()

print("Current date:", current_date)
print("Current time:", current_time)