import os, sys, time, keyboard, pendulum, curses


#Converts Seconds to Microseconds
def secToMili(sec):
    return sec * 1000


#Converts Microseconds to Miliseconds
def microToMili(micro):
    return round(micro / 1000, 2)


#Demands that user runs with sudo, the Curses library seems to require root privileges.
if os.geteuid() != 0:
    print("This script requires superuser privileges. Please run it with sudo.")
    sys.exit(1)

#Gets user input regarding test scope.
key_count = int(input("How many keypresses would you like to test?\nA higher number will take longer, but will yield a more precise output.\nEnter an integer value from 1-1000:"))
timestamps = []

#Collects timestamps correlating to delay between keypresses while holding a key.
for current in range(key_count):
    keyboard.wait('Space')
    timestamps.append(pendulum.now().microsecond)



#Might reference later, will be removing this eventually.
'''
#Time is now converted to ms and this is clearly displayed to the user.
one = pendulum.now()
time.sleep(0.5)
two = pendulum.now()
three = (two - one)
print (str(secToMili(three.seconds) + (microToMili(three.microseconds))) + "ms")
'''
