import time
from datetime import datetime
from plyer import notification


if __name__=="__main__":
    times=["21:56:00","21:58:00"]

    condition = True
    while condition:
        c=datetime.now()
        current_time = c.strftime('%H:%M:%S')
        for i in times:
            if current_time==i:
                notification.notify(
                    title = "Reminder",
                    message = "Work",
                    timeout = 2 #displaying time
                )

                time.sleep(5)
                times.remove(i)
        if times==[]:
            condition = False
