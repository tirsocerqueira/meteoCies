import time
import subprocess
def run_every_10_minutes():
    subprocess.call(["python", "tweet.py"])
    subprocess.call(["python", "animations.py"])
    print("Tweet enviado correctamente")


#First we run 1-time codes
subprocess.call(["python", "tweet_water_variables.py"])
subprocess.call(["python", "tweet_videos.py"])
print("Tweets diarios enviado correctamente")

#Cron jobs every 10 minutes
while True:
    run_every_10_minutes()
    time.sleep(600)
