import time
import os.path
import sys

msg = input("Time you want to alart %h:%m:%s:")
try:
    msg1 = int(msg[0:2])
    msg2 = int(msg[3:5])
    msg3 = int(msg[6:8])
except ValueError:
    print('Wrongtype of input:check your input,it must be hour:min:sec type.')
    time.sleep(2)
    sys.exit()
if msg1 >24 or max(msg2,msg3) >60 or min(msg1,msg2,msg3) < 0:
    print('Input time is invalid.A 24 hour time type is supported.')
    time.sleep(2)
    sys.exit()
name = 'reminder.py'
if not os.path.exists(name):
    print('Fail to open the dir or file:check if you got them right.')
    time.sleep(2)
    sys.exit()
time_pre = time.strftime("%H:%M:%S", time.localtime())
time1 = time_pre[0:2]
time2 = time_pre[3:5]
time3 = time_pre[6:8]
t1 = 3600*msg1+60*msg2+msg3
t2 = 3600*int(time1)+60*int(time2)+int(time3)
try:
    time.sleep(t1-t2-1)
except ValueError:
    print("Time you input has passed today!")
    time.sleep(2)
    sys.exit()
while True:
    time_now = time.strftime("%H:%M:%S", time.localtime()) 
    if time_now == msg: 
        os.system('python3 '+name)
        break
    time.sleep(0.55)
    
