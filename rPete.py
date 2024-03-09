import pendulum
import time

timestamps = []
error_margin = []
iterations = 10

for i in range(iterations):
    timestamps.append(pendulum.now())
    time.sleep(0.1)
    timestamps.append(pendulum.now())
    error_margin.append(abs(500000 - abs(timestamps[(i*2)+1].microsecond - timestamps[i*2].microsecond)))
    print("Pass " + str(i))

print("Average error margin was " + str((sum(error_margin) / iterations) / 1000) + "ms.")
