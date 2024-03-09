import pendulum
import time

timestamps = []
error_margin = []
iterations = 10
pause = 0.3
delay = 0


#Converts Seconds to Microseconds
def secToMicro(sec):
    return sec * 1000000


#Converts Microseconds to Miliseconds
def microToMili(micro):
    return micro / 1000


for i in range(iterations):                                                                                             
    #Stores 2 timestamps that are a given interval apart
    timestamps.append(pendulum.now().microsecond)               
    time.sleep(pause)
    timestamps.append(pendulum.now().microsecond)                                                                                
   

    #Normalize the delay and handles negative values
    if (timestamps[i*2+1] - timestamps[i*2] > 0):
        delay = timestamps[i*2+1] - timestamps[i*2]
    else:
        delay = secToMicro(1) + (timestamps[i*2+1] - timestamps[i*2])
    #Calculates the error margin
    error_margin.append(int(delay - (secToMicro(pause))))
   

    #Let the user know how far along we are. 
    print("Pass " + str(i))
 
#Final result.
print("Average error margin was " + str(microToMili(sum(error_margin) / iterations)) + "ms.")
