class Car:
    def __init__(self, model, color, speed,):
        self.model = model
        self.color = color
        self.speed = speed
        self.passengers = []

    def info(self):
        print(f"автомобіль: {self.model}")
        print(f"колір: {self.color}")
        print(f"швидкість: {self.speed}")
        print(f"пасажири: {self.passengers}")
    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_passenger(self):
        print(f"In the car {self.model}:")


class Passenger:
    def __init__(self, name, phone, height):
        self.name = name
        self.phone = phone
        self.height = height

    def info(self):
        print(f"ім'я пасажира: {self.name}")
        print(f"номер телефона пасажира: {self.phone}")
        print(f"висота пасажира: {self.height}")



car = Car(model="Audi", color="white", speed="240")
car.info()



oleg = Passenger(name="Олег", phone="9961734732173", height="180")
oleg.info()

Ilon = Passenger(name="Ілон", phone="341234123213231", height="190")
Ilon.info()

car.show_passenger()
car.add_passenger(oleg)
car.add_passenger(Ilon)
