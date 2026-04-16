from playsound3 import playsound
import random
import time
import subprocess

min_length=30#in seconds        these both are inclusive, meaning that they can be chosen
max_length=60#in seconds

while True:
    try:
        interval=random.randrange(min_length, max_length+1)
        time.sleep(interval)
        playsound("meow.mp3")
    except:
        subprocess.run("msg * meow.py crashed", shell=True)
