from datetime import datetime

date_birth= input("What is your date of birth (YYYY-MM-dd)")

def parse_time(time):
    return datetime.strptime(time, "%Y-%m-%d")

start_date =parse_time(date_birth)
end_date = datetime.now()
diff=end_date-start_date
print(f"There are {diff.days} days from {start_date} to {end_date}")
print(f"There are {int(diff.total_seconds())} seconds from {start_date} to {end_date}")
