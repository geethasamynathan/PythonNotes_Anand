# in the previous example available seat if you set 2 
#it was assigned 2 seats for Raghula and 1 seat for sonam
# it should be allocated 3 seatas when available seats are 2

from threading import Thread, current_thread, Lock

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat
        self.lock = Lock()  # Create a lock to ensure only one thread modifies the seats at a time
        
    def reserve(self, need_seat):
        with self.lock:  # Ensure that the block of code is executed by only one thread at a time
            print('Available Seats:', self.available_seat)
            if self.available_seat >= need_seat:
                name = current_thread().name
                print(f'{need_seat} seat is allotted for {name}')
                self.available_seat -= need_seat
            else:
                print('Sorry! All seats are allotted')

# Create a Flight object with 2 available seats
f = Flight(2)

# Create two threads to reserve seats
t1 = Thread(target=f.reserve, args=(1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(1,), name='Sonam')

# Start both threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print(f'Final available seats: {f.available_seat}')