class Car:



    def __init__(self, model, color, speed, ):

        self.model = model
        self.color = color
        self.speed = speed

    def info(self):
        print(f"автомобіль: {self.model}")
        print(f"колір: {self.color}")
        print(f"швидкість: {self.speed}")

class Passenger:

    def __init__(self, passenger, phone, height):
        self.passenger = passenger
        self.phone = phone
        self.height = height

    def info(self):
        print(f"ім'я пасажира:{self.passenger}")
        print(f"номер телефона пасажира:{self.phone}")
        print(f"висота пасажира:{self.height}")
Олег = passenger(phone: "9961734732173", height: "180")
Олег.info()


audi = Car(Model:"RX7", color:"White",speed:280)
audi.info()