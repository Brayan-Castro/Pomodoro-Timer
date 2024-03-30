import time
import pyautogui as alrt
# new pc test commit
def main():
    print("*********** Welcome to my Pomodoro Timer! ***********")
    print("")
    usrInput = input("Do you want to start the timer? (y/n) ")

    def pomodoroTimer(base, study = 50, rest = 10):
        restTimer = 0
        while True:
            timer = int(time.time())

            if (timer == base + (study * 60)):
                alrt.alert(text="time to rest!!", title="Pomodoro")
                restTimer = int(time.time())
                hostsCleaner()

            elif (timer == restTimer + (rest * 60)):
                alrt.alert(text="time to study!!", title="Pomodoro")
                base = int(time.time())
                websiteBlocker()

    if usrInput == 'y':
        print("Timer is running!")
        base = int(time.time())
        websiteBlocker()
        pomodoroTimer(base)
    else:
        exit()

def websiteBlocker():
    hosts = open("/mnt/c/Windows/System32/drivers/etc/hosts", "r+")
    content = hosts.read()
    siteList = ["www.youtube.com", "www.reddit.com", "www.instagram.com"]

    for site in siteList:
        if site in content:
            print("already blocked")
            pass
        else:
            hosts.write(f"127.0.0.1     {site}\n")

def hostsCleaner():
    new = open("/mnt/c/Windows/System32/drivers/etc/hosts", "w")
    new.close()

try:
    if __name__ == '__main__':
        main()
except KeyboardInterrupt:
    hostsCleaner()
    print("\nThank you for using!")
    quit()