"""
Write a program to that gets the current time, checks whether it is 12-hour format or 24-hour format.

Change from 12 hour format to 24 hour format, and 24 hour format to 12 hour format.
"""

from datetime import datetime

def is_12_hour_format(time_str):
    try:
        datetime.strptime(time_str, "%I:%M %p")
        return True
    except ValueError:
        return False


def is_24_hour_format(time_str):
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False


def convert_12_to_24(time_str):
    return datetime.strptime(time_str, "%I:%M %p").strftime("%H:%M")


def convert_24_to_12(time_str):
    converted_time = datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p") 
    #return datetime.strptime(time_str, "%H:%M").strftime("%I:%M %p")
    print(f"converted_time in function: {converted_time}")


# Driver Code

if __name__ == "__main__":
    current_time = datetime.now().strftime("%H:%M")
    # current_time = "10:42 PM"
    print(f"Current time {current_time}")

    if is_24_hour_format(current_time):
        print("The Current time is a 24-hour format")
        converted_time = convert_24_to_12(current_time)
        print(f"The Converted time = {converted_time}")

    elif is_12_hour_format(current_time):
        print("The current time is in 12-hoiur format")
        converted_time = convert_12_to_24(current_time)
        print(f"The Converted time = {converted_time}")

    else:
        print("The current_time format is urecognized")


