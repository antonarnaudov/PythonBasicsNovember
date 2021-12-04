pages_count = int(input())
pages_per_hour = int(input())
read_due_days = int(input())

book_reading_hours = pages_count / pages_per_hour
hours_per_day = book_reading_hours / read_due_days

print(round(hours_per_day))
