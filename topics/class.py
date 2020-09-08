"""
str() built-in function uses __str__ to display the string representation of the object
while the repr() built-in function uses __repr__ to display the object.
"""
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @staticmethod
    def stmt(a):
        print(a)
        return True
    # def getvalue(self):
    #     return f"{self.name} is {self.age} years old"

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def __repr__(self):
        return f"{self.name} is {self.age} years old repr"

    def speak(self, sound="Arf"):
        return f"{self.name} says parents  {sound}"

a = Dog("jse", 5)
print(a)
print(repr(a))
print("----")
print(Dog.stmt(5)) #called by class name
print(a.speak("wow")) #called by object only
print("-----")


# >>jse is 5 years old
# >>jse is 5 years old repr


#inheretance
#same function in parent and child class, by defult child classs function will be call, supper() is used to call parent call function
class JackRussellTerrier(Dog):
    def run(self, speed="30"):
        return f"{self.name} speed {speed}"
    def speak_callparent(self, sound="abc"):
        return super().speak()
    def speak(self, sound="Arf"):
        return f"{self.name} says child {sound}"

miles = JackRussellTerrier("Miles", 4)
print(miles.speak("vou"))
print(miles.run("100"))
print(miles.speak_callparent("wow"))
# parent = Dog("Miles2", 4)
# print(parent.speak("vou"))


