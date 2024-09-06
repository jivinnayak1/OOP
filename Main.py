class Car:
    def __init__(self,Wheel,Seat,Engine,Doors,Price):
        self.Wheel = 4
        self.Seat = 5
        self.Engine = Engine
        self.Doors = Doors
        self.Price = Price

BMW = Car(1,4,600000)
Ferrari = Car(1,2,5000000)

print(BMW.Wheel)