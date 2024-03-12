import pendulum
import keyboard
import time

#Converts Seconds to Microseconds
def secToMili(sec):
    return sec * 1000


#Converts Microseconds to Miliseconds
def microToMili(micro):
    return round(micro / 1000, 2)

#Time is now converted to ms and this is clearly displayed to the user.
one = pendulum.now()
time.sleep(0.5)
two = pendulum.now()
three = (two - one)
print (str(secToMili(three.seconds) + (microToMili(three.microseconds))) + "ms")
