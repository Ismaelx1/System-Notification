import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Reminder",
            message = "Break Time!",
            timeout = 10
        )
        time.sleep(5)