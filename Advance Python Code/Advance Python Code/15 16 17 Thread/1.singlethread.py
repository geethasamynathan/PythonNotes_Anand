import threading
import time


def single_task():
    print('Task Started')
    time.sleep(2)
    print('Task Completed')

t=threading.Thread(target=single_task)
t.start()
t.join()
print("Main Thread execution completed")