


# namemingling
class Dog:
    species = "Canis familiaris"
    _protected = "Protected variable can use in subclass"
    __private = "Private Variable only use in  same calss"
    c= __private
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def stmt(a):
        print(a)
        return True
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name} is {self.age} years old repr"

    def __speak(self, sound="Arf"):
        return f"{self.name} says parents  {sound}"


a = Dog("jse", 5)
print(a.c)
# print(a.__private)#restricted in python
print(a._Dog__private)#namemingle
print(a._Dog__speak)
print(a.__class__)
print(dir(a))
exit()


# >>jse is 5 years old
# >>jse is 5 years old repr


# inheretance
# same function in parent and child class, by defult child classs function will be call, supper() is used to call parent call function
class JackRussellTerrier(Dog):
    c = Dog._protected
    def run(self, speed="30"):
        return f"{self.name} speed {speed}"

    def speak_callparent(self, sound="abc"):
        return super().speak()

    def speak(self, sound="Arf"):
        return f"{self.name} says child {sound}"


miles = JackRussellTerrier("Miles", 4)
print(miles.c)
