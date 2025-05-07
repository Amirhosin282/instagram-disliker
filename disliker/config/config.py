# this is func and pips
# this file imported on main file(main.py)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from khayyam import JalaliDate
from colorama import Fore
import sys
import os
from pyfiglet import figlet_format
from rainbowtext import text
import platform

def cl():
    if platform.system() == 'Linux':
        return 'clear'
    elif platform.system() == 'Windows':
        return 'cls'

# var's
date_time = JalaliDate.today() # jalali date
#

if __name__ == '__main__': # sey to user
    os.system(cl())
    print(Fore.RED, 'run main.py, this is not main file ')
    sleep(5)
    sys.exit()

line = "_________________________________________________________________                                                                                             "


def view(a): # app banner

    os.system(cl())

    print(Fore.GREEN)
    print(a)

    print(text(figlet_format("AMIRHOSIN282", font="slant")))

    print(Fore.BLUE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(Fore.RED, "instagram disliker ")

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")

    print(Fore.RED,'    time',Fore.GREEN, a)
    print(Fore.RED,'    email',Fore.GREEN,' amirhosinasdpwr@gmail.com')

    print(Fore.RED,'    by',Fore.BLUE,' amirhosin282')
    print(Fore.WHITE)

    print(Fore.YELLOW)
    print("_________________________________________________________________                                                                                             ")