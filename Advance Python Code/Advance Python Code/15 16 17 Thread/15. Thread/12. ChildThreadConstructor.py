# Creating a thread by creating a child class to Thread class
# Importing Thread Class from threading Module
from threading import Thread

class Mythread(Thread):
	def __init__(self):
		#Thread.__init__(self)		# Calling Thread Class(Parent) Constructor
#Explanation: 📝  
		# if you comment and runt the above line you will get an error. 
		# __init__() method: In the constructor (__init__) of your 
  		# Mythread class, you're not calling the constructor of the 
    	# parent class (Thread) to initialize the thread properly. 
     # This is necessary to set up the thread’s internal state, 
     # which includes attributes like the target function to run. 
     # If you don't  call the parent constructor, the thread won't be initialized 
     # correctly.
		print("Child Thread Constructor")
	def run(self):
		print('Child thread is Running')

t = Mythread()
t.start()
print("Main Thread")
