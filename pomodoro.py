import time
import pyautogui as alrt
import sys

usrInput = input("Do you want to start the timer? (y/n) ")

def holder():
    base = int(time.time())
    pomodoroTimer(base)

def pomodoroTimer(base):
    restTimer = 0
    while True:
        timer = int(time.time())

        if (timer == base + 3000):
            alrt.alert(text="time to rest!!", title="Pomodoro")
            restTimer = int(time.time())
        elif (timer == restTimer + 600):
            alrt.alert(text="time to study!!", title="Pomodoro")
            base = int(time.time())

if usrInput == 'y':
    holder()
else:
    exit()
