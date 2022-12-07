class Car:
    def __init__(self, name, type, kp, motor):
        self.name = name
        self.type = type
        self.kp1 = kp
        self.motor = motor
        self.numberWell = 4

    def move(self, speed):
        print(f"move {self.name} {speed}km/h")

    def signal(self):
        print(f'{self.name} beep-beep')

car1 = Car("Tesla","HB", "Auto", "Electric")
car2 = Car("Porshe","Sedan", "Manual", "Dizel")

car1.move(250)
car2.signal()

print(car1.kp1)
print(car2.motor)