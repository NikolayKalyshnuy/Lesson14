class Car:
    def __init__(self, type, kp, motor):
        self.type = type
        self.kp1 = kp
        self.motor = motor

car1 = Car("HB", "Auto", "Electric")
car2 = Car("Sedan", "Manual", "Dizel")

print(car1)