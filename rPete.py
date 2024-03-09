import pendulum
import time

timestamps = []
error_margin = []
delay = 0

#Gets user input
iterations = int(input("How many iterations would you like to run?\n"))
pause = float(input("How long would you like the pause between tests to be? (In Seconds) 0.01 - 0.99\n"))


#Converts Seconds to Microseconds
def secToMicro(sec):
    return sec * 1000000


#Converts Microseconds to Miliseconds
def microToMili(micro):
    return round(micro / 1000, 2)


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
