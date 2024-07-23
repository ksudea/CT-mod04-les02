from city_management import Vehicle, Event
# Task 1 demo script
car_1 = Vehicle(949, "car", "Sude")
car_2 = Vehicle(6784, "car", "David")
motorcycle_1 = Vehicle(5893, "motorcycle", "Candice")
car_1.update_owner("Lena")
motorcycle_1.update_owner("David")
print(f"New owner of car 1 is {car_1.owner}")
print(f"New owner of motorcycle 1 is {motorcycle_1.owner}")

# Task 2 script
party1 = Event("Sude Bday Party", "07/11")
party1.add_participant(20)
print(f"{party1.name} participant count is {party1.get_participant_count()}")