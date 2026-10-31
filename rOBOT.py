
import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.battery = 100
        self.batteries_count = 5
        self.batteries_spent = 0

    def say_hello(self):
        print(f"Привіт я {self.name}, рівень батареї: {self.battery}% кількість батарейок: {self.batteries_count}/5, витрачено: {self.batteries_spent}).")

class CleanerRobot(Robot):
    def clean(self):
        if self.batteries_count > 0:
            self.batteries_count -= 1
            self.batteries_spent += 1
            self.battery -= 20
            print(f"{self.name} прибирає. Витрачено 1 батарейку🔋! Заряд: {self.battery}% (витрачено загалом: {self.batteries_spent}).")
        else:
            print(f"{self.name} розряджений! Потрібна підзарядка.")


walli = CleanerRobot("Валлі")


walli.say_hello()


cleaning_sessions = random.randint(1, 5)

for _ in range(cleaning_sessions):
    walli.clean()

print("\nРобота закінчена")
walli.say_hello()