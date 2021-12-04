exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_time = exam_min + exam_hour * 60
arrival_time = arrival_min + arrival_hour * 60
diff = exam_time - arrival_time

# Check if he is late
if diff < 0:
    print('Late')
    diff = abs(diff)
    if arrival_time != exam_time:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours after the start")
        else:
            print(f"{minutes} minutes after the start")

# Check if he is on time
elif diff <= 30:
    print('On time')
    if diff > 0:
        print(f"{diff} minutes before the start")

# Check if he is early
else:
    print('Early')
    if arrival_time != exam_time:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f"{hours}:{minutes:02d} hours before the start")
        else:
            print(f"{minutes} minutes before the start")
