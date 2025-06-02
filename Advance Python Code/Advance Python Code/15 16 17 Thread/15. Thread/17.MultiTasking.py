from threading import Thread, current_thread

class Flight:
    def __init__(self, available_seat):
        self.available_seat = available_seat  # No Lock

    def reserve(self, need_seat):
        print(f'Available Seats: {self.available_seat}')
        
        if self.available_seat >= need_seat:
            name = current_thread().name
            print(f'{need_seat} seat(s) allocated for {name}')
            self.available_seat -= need_seat  # Shared resource modification
        else:
            print(f'Sorry {current_thread().name}, not enough seats available!')

# Input
available_seat = 3
customer1 = 1
customer2 = 2

f = Flight(available_seat)

# Create Threads
t1 = Thread(target=f.reserve, args=(customer1,), name='Rahul')
t2 = Thread(target=f.reserve, args=(customer2,), name='Sonam')

# Start Threads
t1.start()
t2.start()

t1.join()
t2.join()

print(f'Final available seats: {f.available_seat}')
