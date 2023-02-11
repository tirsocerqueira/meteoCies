import time
import subprocess
def run_every_10_minutes():
    subprocess.call(["python", "tweet.py"])
    print("Script ran successfully!")

while True:
    run_every_10_minutes()
    time.sleep(600)
