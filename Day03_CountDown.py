import time
def CountDown(t):
    while t:
        min, sec = divmod(t, 60)    
        timer = '{:02d} : {:02d}'.format(min, sec)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("00 : 00")
    print("finished")
t = input("Enter Time in Seconds: ")
CountDown(int(t))
