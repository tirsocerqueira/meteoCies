import time
import subprocess
def run_every_10_minutes():
    subprocess.call(["python", "tweet.py"])
    print("Tweet enviado correctamente")

while True:
    run_every_10_minutes()
    time.sleep(600)
