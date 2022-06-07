#make a program that asks the user for a list of things to do, then asks how many hours they want to work for the day and divide the time evenly amongst the tasks.
#then it should print out the list of things to do, then the number of hours they should work on each thing.
import time
import datetime
import os


to_do_list = input("What is everything you would like to work on today? ")
how_long = float(input("How many hours would you like to work on this? "))


#convert each item in to_do_list into a list
def make_list(to_do):
    li = list(to_do.split(", "))
    return li
   
todays_list = (make_list(to_do_list))
str1 = ', '.join(todays_list)

#evenly divide the number of items in the list to_do_list by the integer of how_long
def divide_time(tasks, hours):
    time_per_task = hours / len(tasks)
    return time_per_task

time_divide = divide_time(todays_list, how_long)

os.system('cls' if os.name == 'nt' else 'clear')
print("Today's list: " + str1)
print("You should work on each task for " + str(time_divide) + " hours.")

time.sleep(2)

input("Press enter to start your first task: ")

#timer for the task at hand
def countdown(h):
    total_seconds = h * 3600
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="\r")
        time.sleep(1)
        total_seconds -= 1
    print("Bzzzt! Time to move on to the next task!")
    input("Press enter to continue: ")

#create a loop through the list of things to do
for i in todays_list:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You are working on: " + i)
    countdown(time_divide)
os.system('cls' if os.name == 'nt' else 'clear')
print("You have completed your day!")