import time
from plyer import notification
while True:
    notification.notify(
        title="Drink Water!",
        message="It's time to drink water.",
        app_icon="water.ico",
        timeout=10
    )
    time.sleep(60*60)