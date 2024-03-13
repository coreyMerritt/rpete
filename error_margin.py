#This program tests the accuracy of the pendulum and time libraries and concludes that the error margin
#is approximately 0.3ms to 1.3ms and seems highly dependant on the delay given to the sleep() function
#inside the time library. This margin seems plenty small enough to use these libraries for rPete.
import pendulum, time

#Converts Seconds to Microseconds
def secToMicro(sec):
    return sec * 1000000


#Converts Microseconds to Miliseconds
def microToMili(micro):
    return round(micro / 1000, 2)


timestamps = []
error_margin = []
delay = 0

#Gets user input
iterations = int(input("How many iterations would you like to run?\nEnter an integer value from: 1 - 999\n"))
pause = float(input("How long would you like the pause between tests to be? (In Seconds)\nEnter a decimal value from: 0.01 - 0.99\n"))


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
    print("Pass " + str(i+1))
 
#Final result.
print("Average error margin was " + str(microToMili(sum(error_margin) / iterations)) + "ms.")
