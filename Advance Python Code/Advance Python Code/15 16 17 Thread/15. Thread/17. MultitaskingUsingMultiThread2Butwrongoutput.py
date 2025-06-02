# Multitasking using Multiple Thread
# Two Threads acting on same method
from threading import Thread, current_thread
class Flight:
	def __init__(self, available_seat):
		self.available_seat = available_seat
		
	def reserve(self, need_seat):
		print('Available Seats:', self.available_seat)
		if(self.available_seat >= need_seat):
			name = current_thread().name
			print(f'{self.available_seat} seat is alloted for {name}')
			self.available_seat -= need_seat
			
		else:
			print('Sorry! All seats has alloted')
available_seat=int(input('Enter the available Seat'))
customer1=int(input('Enter the no.of.seats you need'))
customer2=int(input('Enter the no.of.seats you need'))

f = Flight(available_seat)
t1 = Thread(target=f.reserve, args=(customer1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(customer2,), name='Sonam')
t1.start()
t2.start()

