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
#Lets just check the math one step at a time. For starters I should move to storing only the microsecond values into the timestamps list, storing the
#entire timestamp was just silly and can only hurt our error margin. These changes are also reflected above now.
timestamps.append(pendulum.now().microsecond)
time.sleep(pause)
timestamps.append(pendulum.now().microsecond)

print(timestamps[0])
print(timestamps[1])
print(timestamps[1]- timestamps[0])
