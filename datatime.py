from datetime import datetime

loop_controller = True
while loop_controller:
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    if current_time == '06:01:00':
        print("Your Requrested Current Time =", current_time)
        loop_controller = False