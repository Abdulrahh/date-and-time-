# code to check if the current date and time has passed a certain date and time 
# p.s this file runs an infinite loop proceed with caution 
import datetime
import time 

target_datetime = datetime.datetime(9999, 2, 4, 12, 14, 0) 

while True:
    current_datetime = datetime.datetime.now()
    if target_datetime >  current_datetime:
        day = target_datetime - current_datetime
        with open("coundown.txt", "a") as file:
             file.write(str(day) + "\n") #appends the infinite loop to a file 
        time.sleep(0.1)
       
    
    elif target_datetime < current_datetime:
        print("Past")
        break
    
    else:
        print("same time") #condition not gonna work cus it icludes microseconds  so it never true 






