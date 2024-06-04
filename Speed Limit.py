## Time and Speed Problem

# User Inputs
avg_speed = int(input("What is your average speed (in mph)? "))
speed_limit = int(input("What is the posted speed limit (in mph)? "))
distance = float(input("What is the distance traveled? "))

# Calculations
at_limit_time = distance / speed_limit
over_limit_time = distance / avg_speed

time_saved_hr = at_limit_time - over_limit_time
time_saved_min = time_saved_hr * 60

# Output
if avg_speed > speed_limit:
    print("oh you fast, huh?")
    print(f"You saved {time_saved_min:.1f} minutes traveling at {avg_speed}mph instead of the posted speed limit ({speed_limit}mph).")
elif avg_speed <= speed_limit:
    print("No time saved going at or below posted speed limit.")
