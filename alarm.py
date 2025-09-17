import datetime
import time
from playsound import playsound  # install with: pip install playsound==1.2.2

def set_alarm():
    alarm_time = input("Set alarm time (HH:MM:SS AM/PM): ").strip()
    try:
        alarm_hour, alarm_minute, alarm_second_period = alarm_time.split(":")
        alarm_second, period = alarm_second_period.split()

        alarm_hour = int(alarm_hour)
        alarm_minute = int(alarm_minute)
        alarm_second = int(alarm_second)
        period = period.upper()

        if period == "PM" and alarm_hour !_
