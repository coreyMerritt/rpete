import os, sys, time, keyboard, pendulum, curses


#Converts Seconds to Microseconds.
def secToMili(sec):
    return sec * 1000

#Converts Seconds to Microseconds.
def secToMicro(sec):
    return sec * 1000000

#Converts Microseconds to Miliseconds.
def microToMili(micro):
    return round(micro / 1000, 2)


#Demands that user runs with sudo, the Curses library requires root privileges.
if os.geteuid() != 0:
    print("This script requires superuser privileges. Please run it with sudo.")
    sys.exit(1)


#Gets user input regarding test scope.
key_count = int(input("How many keypresses would you like to test?\nA higher number will take longer, but will yield a more precise output.\nEnter an integer value from 1-1000:\n"))
timestamps = []


#Prompts the user to hold a key to collect repeat rate/delay data.
print("Press and hold the Spacebar key when ready.\nDo not stop until the program proceeds.")


#Hides keystrokes from the user for a cleaner look.
stdscr = curses.initscr()


#Collects timestamps correlating to delay between keypresses while holding a key.
last_ts = pendulum.now()
for current in range(key_count):
    keyboard.wait('Space')
    timestamps.append(pendulum.now().microsecond)
    if ((pendulum.now() - last_ts).seconds > 1):                        #Checks for user error.
        print("You let go of the space key. Please try again.")
        stdscr.clear()
        curses.endwin()
        sys.exit()
    last_ts = pendulum.now()


#Stops hiding the user's keystrokes.
stdscr.clear()
curses.endwin()


repeat_rate = []
repeat_delay = 0

#Appends normalized delay after handling negative values.
for i in range(1, len(timestamps)):
    if i == 1:
        if (timestamps[i] - timestamps[i-1] > 0):
            repeat_delay = (timestamps[i] - timestamps[i-1])
        else:
            repeat_delay = (secToMicro(1) + (timestamps[i] - timestamps[i-1]))
    else:
        if (timestamps[i] - timestamps[i-1] > 0):
            repeat_rate.append(timestamps[i] - timestamps[i-1])
        else:
            repeat_rate.append(secToMicro(1) + (timestamps[i] - timestamps[i-1]))


rr_total = 0

#Calculates the average repeat rate from all values in the list.
for x in repeat_rate:
    rr_total += x
rr_avg = rr_total / len(repeat_rate)


#Displays the result to the user.
print("Your repeat delay is: " + str(int(microToMili(repeat_delay))) + "ms")
print("Your repeat rate is: " + str(int(microToMili(rr_avg))) + "ms")
