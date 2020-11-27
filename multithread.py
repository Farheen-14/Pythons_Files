# Multithreading 
# its like a multitasking at the same time..
# example - in computer we are using many function at same time like word - we are typing saving spell check at the same time so they are seperated work with thread 
# one work = one thread 

# run the program at the same time so its called threading or multi threading.

from time import sleep      # Sleep library for timing
from threading import *     #import the library or module name is- threading 
class Hello(Thread):
    def run(self):      #run is the fucntion for threading..
        for i in range(5):
            print("Hey! Farheen")
            sleep(1)       #sleep()- for timing to run the program
class Hi(Thread):
    def run(self):
        for i in range(5):
            print("How are you")
            sleep(1)
h1 = Hello()
h2 = Hi()

h1.start()
sleep(0.2)  #The time between function1 and function2, 
h2.start()
sleep(0.2)

h1.join()        #join- thread run one by one, not interfaring the multithread in other threads so we use join, and after both thread run - multithread run.
h2.join()

print("Bye..Have a nice day")   #it is multithreading so it will run...

#here is 3 threading 
# 1st - Multithreading - which we process for all
# 2nd - h1 and 3rd- h2 both are thread 