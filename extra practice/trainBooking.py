class TrainBookingSystem:
    def __init__(self):
        self.trains = {
            1: {'name': 'Express A', 'seats': 50},
            2: {'name': 'Express B', 'seats': 40},
            3: {'name': 'Express C', 'seats': 60}
        }
        self.bookings = {}

    def view_trains(self):
        print("Available Trains:")
        for train_id, train in self.trains.items():
            print(f"{train_id}. {train['name']} - Seats Available: {train['seats']}")

    def book_ticket(self):
        name = input("Enter your name: ")
        self.view_trains()
        train_id = int(input("Select Train ID to book: "))

        if train_id in self.trains and self.trains[train_id]['seats'] > 0:
            self.trains[train_id]['seats'] -= 1
            booking_id = len(self.bookings) + 1
            self.bookings[booking_id] = {'name': name, 'train': self.trains[train_id]['name']}
            print(f"Booking successful! Your Booking ID: {booking_id}")
        else:
            print("Invalid train ID or no available seats.")

    def view_bookings(self):
        print("Your Bookings:")
        for booking_id, booking in self.bookings.items():
            print(f"Booking ID: {booking_id} - Name: {booking['name']} - Train: {booking['train']}")

    def cancel_booking(self):
        booking_id = int(input("Enter Booking ID to cancel: "))
        if booking_id in self.bookings:
            train_name = self.bookings[booking_id]['train']
            for train_id, train in self.trains.items():
                if train['name'] == train_name:
                    train['seats'] += 1
            del self.bookings[booking_id]
            print("Booking cancelled successfully.")
        else:
            print("Invalid Booking ID.")

    def menu(self):
        while True:
            print("\n1. View Trains\n2. Book Ticket\n3. View Bookings\n4. Cancel Booking\n5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_trains()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.view_bookings()
            elif choice == '4':
                self.cancel_booking()
            elif choice == '5':
                print("Thank you for using the Train Booking System!")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = TrainBookingSystem()
    system.menu()
