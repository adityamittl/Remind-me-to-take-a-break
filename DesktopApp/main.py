from browserControl import WebAccess
from time import sleep
from datetime import timedelta, datetime

timelimit = 0 # time in  minutes
future_time = 0
def checkTime():
    if datetime.now() > future_time:
        print("Time is up")
        return True

def main(NAME,LIMIT,PLATFORM):
    timelimit = float(LIMIT)
    future_time = datetime.now() + timedelta(minutes=timelimit)
    print(future_time)
    web = WebAccess() # inititalizing and opening the browser


    # implement open CV here



    if PLATFORM == "youtube":
        web.youtube(NAME)
    elif PLATFORM == "netflix":
        web.Netflix(NAME)

    web.enterFullScreen() # this is to enter full screen mode

    if(checkTime()): # call this with each frame to calculate the remaining time
        web.switchState() # this is to pause the video
    