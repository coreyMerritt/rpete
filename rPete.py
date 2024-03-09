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
#Well I definitely solved this more with logic than math but a win is a win. You can now see that 
#no matter how many times you run this, the output is relatively normalized.
timestamps.append(pendulum.now().microsecond)
time.sleep(pause)
timestamps.append(pendulum.now().microsecond)

print(timestamps[0])
print(timestamps[1])
if (timestamps[1] - timestamps[0] > 0):
    print(timestamps[1] - timestamps[0])
else: 
    print(1000000 + (timestamps[1] - timestamps[0]))    #1000000 is the constant for microseconds in 1s.
