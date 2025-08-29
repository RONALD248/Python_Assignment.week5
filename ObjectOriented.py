#Activity  One: Design a class structure for a smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.__battery = battery   # encapsulated attribute

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def get_battery(self):
        return self.__battery

    def set_battery(self, value):
        if 0 <= value <= 100:
            self.__battery = value
        else:
            print("Invalid battery percentage!")

# Inheritance
class GamingPhone(Smartphone):
    def play_game(self, game):
        print(f"Playing {game} on {self.model}!")

# Test
phone1 = Smartphone("Samsung", "S24", 85)
gaming_phone = GamingPhone("Asus", "ROG 7", 95)

phone1.make_call("0712345678")
gaming_phone.play_game("PUBG")


#Activity Two: Implement polymorphism with different vehicle typesS
class Vehicle:
    def move(self):
        pass  # abstract action

class Car(Vehicle):
    def move(self):
        print("Driving ")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing ")

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()

