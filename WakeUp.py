import time

class Wake(object):
    def onSleep(secs: int = 0):
        time.sleep(secs)

    def onTime():
        return time.strftime("%H:%M:%S")
    
    def onDate():
        return time.strftime("%y-%m-%d")