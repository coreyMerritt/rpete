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


#Demands that user runs with sudo, the Curses library seems to require root privileges.
if os.geteuid() != 0:
    print("This script requires superuser privileges. Please run it with sudo.")
    sys.exit(1)


#Gets user input regarding test scope.
key_count = int(input("How many keypresses would you like to test?\nA higher number will take longer, but will yield a more precise output.\nEnter an integer value from 1-1000:"))
timestamps = []



#Prompts the user to traverse the for loop.
print("Press and hold the Spacebar key when ready.\nDo not stop until the program proceeds.")


#Hides keystrokes from the user for a cleaner look.
curses.initscr()


#Collects timestamps correlating to delay between keypresses while holding a key.
for current in range(key_count):
    keyboard.wait('Space')
    timestamps.append(pendulum.now().microsecond)


#Stops hiding the user's keystrokes.
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

#Debugging
for x in repeat_rate:
    print("Repeat Rate = " + str(x))

print("Repeat Delay = " + str(repeat_delay))




#Might reference later, will be removing this eventually.
'''
#Time is now converted to ms and this is clearly displayed to the user.
one = pendulum.now()
time.sleep(0.5)
two = pendulum.now()
three = (two - one)
print (str(secToMili(three.seconds) + (microToMili(three.microseconds))) + "ms")
'''
