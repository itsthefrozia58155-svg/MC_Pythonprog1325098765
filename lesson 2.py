import random
class Student:

    def __init__(self, name, age):
        self.name  = name
        self.age = age
        self.skill = 1
        self.money = 50

    def study(self):
        self.skill +=1
        print("Studying...")

    def chill(self):
        self.skill -=0.5
        print("😀😁😂🤣😂😃😄😂😀🤣🤣😁🤣😃😂😁😂Chilling...")
    def work(self):
        self.money +=50
        print("😄😄😄😄😄😄😄😄😄😄😄😄😄Working...")

    def info(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")
        print(f"Skills: {self.skill}👺🧐🧐🧐🤓🤓🫣🧐🧐🤓👺🧐🧐")
Oleg = Student("Oleg", 15)
Oleg.info()
for day in range(365):
    choice = random.randint(0, 2)
    if choice == 0:
        Oleg.chill()
    elif choice == 1:
        Oleg.study()
    else:
        Oleg.work()
Oleg.age += 1
Oleg.info()