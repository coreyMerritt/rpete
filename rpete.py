import os, sys, keyboard, pendulum, curses


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


def main(display):
    curses.echo()
    
    #Gets user input regarding test scope.
    display.addstr("How many keystrokes would you like to test? (A higher # will take longer but will be more accurate.)\n")
    display.addstr("\nEnter an integer value from 1-1000:\n")
    display.refresh()
    key_count = int(display.getstr().decode())
    
    curses.noecho()
    while True:
        timestamps = []

        #Prompts the user to hold a key to collect repeat rate/delay data.
        display.clear()
        display.addstr("Press and hold the Spacebar key when ready. Do not release Spacebar until told to.\n")
        display.refresh()
    
        #Collects timestamps correlating to delay between keypresses while holding a key.
        first_pass = True
        user_error = False
        last_ts = pendulum.now()
        for current in range(key_count):
            keyboard.wait('Space')
            timestamps.append(pendulum.now().microsecond)
            if ((pendulum.now() - last_ts).seconds > 1 and first_pass == False):                        #Checks for user error.
                user_error = True
                display.addstr("You let go of the space key. Please try again.")
                display.refresh()
                break
            first_pass = False
            last_ts = pendulum.now()
        if (user_error == False):
            break


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


    #Displays results for user.
    display.clear()
    display.addstr("Your repeat delay is: " + str(int(microToMili(repeat_delay))) + "ms")
    display.addstr("\nYour repeat rate is: " + str(int(microToMili(rr_avg))) + "ms\n")
    display.addstr("\nPress Enter to exit.")
    display.refresh()
    keyboard.wait('Enter')


curses.wrapper(main)
