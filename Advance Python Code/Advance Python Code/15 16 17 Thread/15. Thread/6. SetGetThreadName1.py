# Importing Thread Class from threading Module
from threading import Thread, current_thread

def disp():
	print(f"\nChild Thread {current_thread()}")

	print(f"\nDefault Child Thread Name: {current_thread().getName}")

	#current_thread().setName('Doc Thread') # deprecated
	current_thread().name='Child Doc Thread'
	print(f"\nNew Child Thread Name: {current_thread().getName}")
	
	current_thread().name = 'Child Flying Thread'
	
	print(current_thread().name)
	

# Creating Thread Class Object
t = Thread(target=disp)

# Starting Thread
t.start()

print("\nMain Thread", current_thread())

print("\nDefault Main Thread Name:", current_thread().getName)

current_thread().name='Main Python Demo Thread'
print("\nNew Main Thread Name:", current_thread().getName)

current_thread().name = 'Main Demo Thread'

print()
print(current_thread().name)



