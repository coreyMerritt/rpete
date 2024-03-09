import pendulum
import time

timestamps = []
error_margin = []
iterations = 10
pause = 0.3
delay = 0


for i in range(iterations):                                                                                             
    #Stores 2 timestamps that are a given interval apart.
    timestamps.append(pendulum.now().microsecond)               
    time.sleep(pause)
    timestamps.append(pendulum.now().microsecond)                                                                                
   

    #Normalize the delay and handles negative values; Calculates the error margin.
    if (timestamps[i*2+1] - timestamps[i*2] > 0):
        delay = timestamps[i*2+1] - timestamps[i*2]
    else:
        delay = 1000000 + (timestamps[i*2+1] - timestamps[i*2])     #1000000 is the constant for microseconds in 1s.
    error_margin.append(int(delay - (1000000 * pause)))
   

    #Let the user know how far along we are. 
    print("Pass " + str(i))
 
#Final result.
print("Average error margin was " + str((sum(error_margin) / iterations) / 1000) + "ms.")
