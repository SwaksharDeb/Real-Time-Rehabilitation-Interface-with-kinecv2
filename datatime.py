from datetime import datetime

def target_time(set_time:str):
    loop_controller = True
    while loop_controller:
        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        if current_time == set_time:
            print("Your Requrested Current Time =", current_time)
            loop_controller = False

time = input("Set the target time: ") # '06:24:00'
target_time(time)