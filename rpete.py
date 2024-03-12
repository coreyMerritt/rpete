import pendulum
import keyboard
import time
import curses

#Converts Seconds to Microseconds
def secToMili(sec):
    return sec * 1000


#Converts Microseconds to Miliseconds
def microToMili(micro):
    return round(micro / 1000, 2)


#Lets just start at the beginning, seems sensible.
key_count = input("How many keypresses would you like to test?\nA higher number will take longer, but will yield a more precise output.\nEnter an integer value from 1-1000:")





#Might reference later, will be removing this eventually.
'''
#Time is now converted to ms and this is clearly displayed to the user.
one = pendulum.now()
time.sleep(0.5)
two = pendulum.now()
three = (two - one)
print (str(secToMili(three.seconds) + (microToMili(three.microseconds))) + "ms")
'''
