import time
import pyautogui as alrt

print("*********** Welcome to my Pomodoro Timer! ***********")
print("")
 
try:
    stTime = int(input("How much study time (default = 50min)? "))
    rsTime = int(input("How much resting time (default = 10min)?"))
except ValueError:
    print("Error: input isn't a number, please try again")
    exit()

print("")
usrInput = input("Do you want to start the timer? (y/n) ")

def holder():
    base = int(time.time())
    pomodoroTimer(base, stTime, rsTime)

def pomodoroTimer(base, study = 50, rest = 10):
    restTimer = 0
    while True:
        timer = int(time.time())

        if (timer == base + (study * 60)):
            alrt.alert(text="time to rest!!", title="Pomodoro")
            restTimer = int(time.time())
        elif (timer == restTimer + (rest * 60)):
            alrt.alert(text="time to study!!", title="Pomodoro")
            base = int(time.time())

if usrInput == 'y':
    print("Timer is running!")
    holder()
else:
    exit()