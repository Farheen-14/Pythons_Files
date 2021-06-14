# import threading
# print("This is first threading : ",threading.current_thread().getName())

# Q.make a multithreading program without class

from threading import *
def display():
    for i in range(10):
        print("Hello Next Prime Minister....this is from child")
t= Thread(target=display)
t.start()
for i in range(10):
    print("This is from multithread...")



