import webbrowser
import time

break_count=0
total_breaks=3
work_time_lenght=25
break_time_lenght=5

print("This program started at: "+time.ctime())

while (break_count<total_breaks):
    print("Please resume working")
    print("Current time: "+time.ctime())
    time.sleep(work_time_lenght*60)

    print("Please take a break")
    print("Current time: "+time.ctime())
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(break_time_lenght*60)
    
    break_count = break_count + 1
