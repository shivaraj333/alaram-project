from datetime import datetime
from playsound import playsound
alarm_time=input("enter the time tobe set as HH:MM:SS:period\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_second=alarm_time[6:8]
alarm_period=alarm_time[9:11].upper()
print("alarm is setting ")
while True:
    current_time=datetime.now()
    current_hour=current_time.strftime("%I")
    current_minute=current_time.strftime("%M")
    current_second=current_time.strftime("%S")
    current_period=current_time.strftime("%p")
    if(current_period == alarm_period):
        if(current_hour == alarm_hour):
            if(current_minute == alarm_minute):
                if(current_second == alarm_second):
                    print("wake up call!...")
                    playsound('/Shttps://www.soundsnap.com/search/audio?query=alarm#/note.wav')
                    break

