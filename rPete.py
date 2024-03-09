import pendulum
import time

timestamps = []
error_margin = []
iterations = 10
pause = 0.3

'''
for i in range(iterations):                                                                                             
    #Stores 2 timestamps that are a given interval apart.
    timestamps.append(pendulum.now().microsecond)               
    time.sleep(pause)
    timestamps.append(pendulum.now().microsecond)                                                                                
    
    #Debugging
    print(str(abs((pause * 1000000) - abs(timestamps[(i*2)+1] - timestamps[i*2]))) + " ~800")
    
    #(ts2 - ts1) - expected interval = error margin 
    error_margin.append(abs((pause * 1000000) - abs(timestamps[(i*2)+1].microsecond - timestamps[i*2].microsecond)))
   
    #Let the user know how far along we are. 
    print("Pass " + str(i))

#Final result.
print("Average error margin was " + str((sum(error_margin) / iterations) / 1000) + "ms.")
'''

#Debugging
#Moved the delay into a proper variable. This will make further manipulation of our figure more readable as we move forward.
timestamps.append(pendulum.now().microsecond)
time.sleep(pause)
timestamps.append(pendulum.now().microsecond)

print(timestamps[0])
print(timestamps[1])

delay = 0

if (timestamps[1] - timestamps[0] > 0):
    delay = timestamps[1] - timestamps[0]
else: 
    delay = 1000000 + (timestamps[1] - timestamps[0])    #1000000 is the constant for microseconds in 1s.

print(delay)
