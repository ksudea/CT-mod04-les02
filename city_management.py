#Task 1
class Vehicle:

    def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
    
    def update_owner(self, new_owner):
          self.owner = new_owner

#Task 2
class Event:
    def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0
    
    def add_participant(self, amount=1):
          self.participant_count += amount
    
    def get_participant_count(self):
          return self.participant_count