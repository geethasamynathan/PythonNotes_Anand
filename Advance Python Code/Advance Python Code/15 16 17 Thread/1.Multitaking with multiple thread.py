import threading
import time

def task1():
    for i in range(5):
        print(f"Task 1 -count {i}")
        time.sleep(1)
        
        
def task2():
    for i in range(5):
        print(f"Task 2 -Count ={i}")
        time.sleep(1)
    
thread1=threading.Thread(target=task1)
thread2= threading.Thread(target=task2)

thread1.start()
thread2.start()

#thread1.join()
#thread2.join()

print("Both the tasks completed")