import pendulum
import time

timestamps = [pendulum.now()]
print(timestamps[0].microsecond)

time.sleep(0.5)

timestamps.append(pendulum.now())
print(timestamps[1].microsecond)

print(abs(500000 - abs(timestamps[1].microsecond - timestamps[0].microsecond)))
