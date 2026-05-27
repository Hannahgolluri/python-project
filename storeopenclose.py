# Store opening and closing time (24-hour format)
open_time = 9   # 9 AM
close_time = 21 # 9 PM

# Get current time from user
current_time = int(input("Enter current time (0-23): "))

# Check if store is open or closed
if current_time >= open_time and current_time < close_time:
    print("Store is OPEN")
else:
    print("Store is CLOSED")
