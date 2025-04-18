#Standby Mode Code Simulation

import time

# Time app has been unused
app_unused_time = 0

# Time app has not shown a notification
app_notification_time = 0

# App is running on mobile device
active_app = True

while(active_app):
    # Simulate the app being unused for a period of time
    app_unused_time += 1
    app_notification_time += 1

    # Check if the app has been unused for 5 minutes (300 seconds)
    if app_unused_time >= 400:
        print("App is now in standby mode due to inactivity. Entering standby mode.")
        break

    # Check if the app has not shown a notification for 10 minutes (600 seconds)
    if app_notification_time >= 100:
        print("App has not shown a notification for a while. Entering standby mode.")
        break

    # Simulate waiting for 1 second before checking again
    time.sleep(1)