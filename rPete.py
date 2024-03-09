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
#Our first real problem can be displayed by running this code. The problem is that if timestamp #2 ticks up the seconds timer, the "microseconds" of timestamp #2 will actually be smaller
#than in timestamp #1, we could add seconds into the mix as well but we'll just run into the same problem when seconds tick over 59, instead I'll be attempting to solve this by playing around
#with a few formulas by intuition.
timestamps.append(pendulum.now().microsecond)
time.sleep(pause)
timestamps.append(pendulum.now().microsecond)

print(timestamps[0])
print(timestamps[1])
print(timestamps[1]- timestamps[0])
