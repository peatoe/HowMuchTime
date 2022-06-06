import time
import datetime
import os


to_do_list = input("What is everything you would like to work on today? ")

def make_list(to_do):
    li = list(to_do.split(", "))
    return li
   
todays_list = (make_list(to_do_list))
str1 = ', '.join(todays_list)
print("Here is what you are working on today: " + str1)

h1 = input("How long do you want to work on " + todays_list[0] + "?")
h2 = input("How long do you want to work on " + todays_list[1] + "?")

os.system('cls' if os.name == 'nt' else 'clear')

print("You are working on: " + todays_list[0])

def countdown(h):
    total_seconds = h * 60
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Bzzzt! Time to move on to: " + todays_list[1])

countdown(int(h1))
