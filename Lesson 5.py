class Parent:
    def __init__(self, eye_color, surname):
        self.eye_color = eye_color
        self.surname = surname


    def info(self):
        print(f"My surname is {self.surname}.I have {self.eye_color} eyes.")

    def cooking(self):
        print("Cook delicious meat🥩🥩🥩")

class Son(Parent):
    def programming(self):
        print("I'm a python developer😊")

print("+++++++++FATHER+++++++++++")
oleg = Parent("Gray","Zaycev")
oleg.info()
oleg.cooking()

print("++++++++++SON++++++++++")

Ilon = Son("blue","Zaycev")
Ilon.info()
Ilon.programming()
Ilon.cooking()
