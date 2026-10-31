class Car:
    def __init__(self, model, color, speed):
        self.model = model
        self.color = color
        self.speed = speed
        self.passengers = []

    def info(self):
        print(f"Автомобіль: {self.model}")
        print(f"Колір: {self.color}")
        print(f"Швидкість: {self.speed}")
        print("Список пасажирів у машині:")
        for passenger in self.passengers:
            print(f"  - Ім'я: {passenger.name}")
            print(f"    Телефон: {passenger.phone}")
            print(f"    Зріст: {passenger.height}")

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def show_passengers(self):
        print(f"У машині {self.model}:")
        for passenger in self.passengers:
            passenger.info()


class Passenger:
    def __init__(self, name, phone, height):
        self.name = name
        self.phone = phone
        self.height = height

    def info(self):
        print(f"Ім'я пасажира: {self.name}")
        print(f"Номер телефону: {self.phone}")
        print(f"Зріст: {self.height}")


# Створюємо об'єкт машини
car = Car(model="Audi", color="white", speed="240")

# Створюємо пасажирів (телефон і зріст передаються як окремі параметри)
oleg = Passenger(name="Олег", phone="9961734732173", height="180")
ilon = Passenger(name="Ілон", phone="341234123213231", height="190")

# Виводимо інформацію про кожного пасажира окремо за допомогою їхнього методу info()
print("--- Інформація про пасажирів окремо ---")
oleg.info()
print()
ilon.info()
print()

# Додаємо пасажирів до машини
car.add_passenger(oleg)
car.add_passenger(ilon)

# Виводимо загальну інформацію про машину разом із її пасажирами
print("--- Інформація про автомобіль та пасажирів у ньому ---")
car.info()