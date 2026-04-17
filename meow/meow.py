import sys
from playsound3 import playsound
import random
import time
import subprocess

min_length=30#in seconds        these both are inclusive, meaning that they can be chosen
max_length=60#in seconds

while True:
    try:
        if sys.argv[1] and sys.argv[2]:
            min_length=int(sys.argv[1])
            max_length=int(sys.argv[2])
            print(min_length," ",max_length)
    except IndexError:
        pass
    try:
        interval=random.randrange(min_length, max_length+1)
        time.sleep(interval)
        playsound("meow.mp3")
    except Exception as e:
        subprocess.run(f"msg * meow.py crashed, {e}", shell=True)
        break

quit()
