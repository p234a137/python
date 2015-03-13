
class Car(object):
    """ car class """
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
    
    def display_car(self):
        text = "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."
        return text

    def drive_car(self):
        """changes the condition member variable"""
        self.condition = "used"


class ElectricCar(Car):
    """ electric car """
    def __init__(self, battery_type):
        self.battery_type = battery_type
    
    def drive_car(self):
        self.condition = "like new"


## my_car = Car("DeLorean", "silver", 88)
## # change of condition after driving car
## print my_car.condition
## my_car.drive_car()
## print my_car.condition

my_car = ElectricCar("molten salt")
my_car.model = "Elantra"
my_car.color = "Gray"
my_car.mpg = 40
print my_car.condition
my_car.drive_car()
print my_car.condition

