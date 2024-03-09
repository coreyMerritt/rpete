import pendulum
import keyboard
import time

#Learning object behavior in pendulum. Pendulum interval objects have all the same elements as datetime
#objects AND can convert minutes into seconds with minimal effort. This outputs "75" just as you'd hope.
one = pendulum.now()
time.sleep(75.5)
two = pendulum.now()
three = (two - one)
print (three.seconds)
